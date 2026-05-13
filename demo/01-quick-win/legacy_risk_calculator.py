"""
Legacy Risk Calculator Module.

Exercise B: Select the entire `calculate_portfolio_var` function below,
open Copilot Chat (Ctrl+Alt+B), and type: /explain
See GUIDE.md for full instructions.
"""

import numpy as np
from datetime import datetime, timedelta


def calculate_portfolio_var(positions, market_data, conf_level=0.95, horizon=10, method='historical', decay=0.94, min_obs=252, adj_factor=None):
    if not positions or not market_data:
        return None
    px = {}
    for sym in positions:
        if sym in market_data and len(market_data[sym]) >= min_obs:
            px[sym] = market_data[sym][-min_obs:]
        else:
            px[sym] = market_data.get(sym, [0] * min_obs)
    
    ret = {}
    for sym, prices in px.items():
        r = []
        for i in range(1, len(prices)):
            if prices[i-1] != 0:
                r.append((prices[i] - prices[i-1]) / prices[i-1])
            else:
                r.append(0)
        ret[sym] = r
    
    if method == 'historical':
        port_ret = []
        n = min(len(v) for v in ret.values()) if ret else 0
        for i in range(n):
            daily = sum(positions[sym] * ret[sym][i] for sym in positions if sym in ret)
            port_ret.append(daily)
        port_ret.sort()
        idx = int(len(port_ret) * (1 - conf_level))
        var = abs(port_ret[idx]) if port_ret else 0
    elif method == 'parametric':
        weights = np.array([decay ** (len(list(ret.values())[0]) - 1 - i) for i in range(len(list(ret.values())[0]))])
        weights = weights / weights.sum()
        syms = list(positions.keys())
        n_assets = len(syms)
        cov = np.zeros((n_assets, n_assets))
        for i in range(n_assets):
            for j in range(n_assets):
                if syms[i] in ret and syms[j] in ret:
                    ri = np.array(ret[syms[i]])
                    rj = np.array(ret[syms[j]])
                    min_len = min(len(ri), len(rj), len(weights))
                    cov[i, j] = np.sum(weights[:min_len] * ri[:min_len] * rj[:min_len])
        pos_vec = np.array([positions[s] for s in syms])
        port_vol = np.sqrt(pos_vec @ cov @ pos_vec)
        z = {0.90: 1.282, 0.95: 1.645, 0.99: 2.326}.get(conf_level, 1.645)
        var = port_vol * z
    else:
        n_sims = 10000
        syms = list(positions.keys())
        sim_returns = []
        for _ in range(n_sims):
            total = 0
            for sym in syms:
                if sym in ret and ret[sym]:
                    sampled = ret[sym][np.random.randint(0, len(ret[sym]))]
                    total += positions[sym] * sampled
            sim_returns.append(total)
        sim_returns.sort()
        idx = int(n_sims * (1 - conf_level))
        var = abs(sim_returns[idx])
    
    var_scaled = var * np.sqrt(horizon)
    if adj_factor:
        var_scaled *= adj_factor
    return round(var_scaled, 2)
