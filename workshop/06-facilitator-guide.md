# Facilitator Guide

## Pre-Workshop Preparation

### 1 Week Before

- [ ] Confirm attendee count and room setup (each person needs a laptop)
- [ ] Send pre-requisites email:
  - Install VS Code
  - Install GitHub Copilot extension (confirm license activation)
  - Install Python 3.9+ with pandas, numpy, pytest
  - Clone the workshop repository (or confirm access to shared drive)
- [ ] Test all demos end-to-end on the presentation machine
- [ ] Prepare backup: screenshots/recordings of every demo in case Copilot is unavailable
- [ ] Confirm projector/screen resolution and adjust font sizes accordingly
- [ ] Prepare synthetic dataset and verify it loads correctly

### 1 Day Before

- [ ] Run through the full 90 minutes (time yourself)
- [ ] Verify Copilot is responding well (check for service issues)
- [ ] Ensure all demo files are in place and clean (reset any previous demo state)
- [ ] Test Wi-Fi / network at the venue (Copilot requires internet)
- [ ] Prepare printed prompt library handouts (optional)
- [ ] Charge laptop, bring adapter/dongle for projector
- [ ] Set VS Code: font size 16+, dark theme, Copilot chat panel visible

### 30 Minutes Before

- [ ] Open all demo files in VS Code tabs (in order)
- [ ] Open Copilot Chat panel
- [ ] Clear chat history from previous sessions
- [ ] Load the dataset and confirm `df` is accessible
- [ ] Set "Do Not Disturb" mode (suppress notifications)
- [ ] Have speaker notes on second monitor or printed

---

## Environment Setup

### Required Software
| Component | Version | Purpose |
|-----------|---------|---------|
| VS Code | Latest stable | IDE |
| GitHub Copilot extension | Latest | AI assistance |
| GitHub Copilot Chat extension | Latest | Chat interface |
| Python | 3.9+ | Runtime |
| pandas | 2.0+ | Data manipulation |
| numpy | 1.24+ | Numerical operations |
| pytest | 7.0+ | Testing |

### Quick Setup Script (for attendees)
```bash
# Create virtual environment
python -m venv copilot-workshop
# Activate (Windows)
copilot-workshop\Scripts\activate
# Activate (macOS/Linux)
source copilot-workshop/bin/activate
# Install dependencies
pip install pandas numpy pytest
```

### VS Code Settings for Presentation
```json
{
  "editor.fontSize": 18,
  "terminal.integrated.fontSize": 16,
  "editor.lineHeight": 1.6,
  "workbench.colorTheme": "Default Dark Modern",
  "editor.minimap.enabled": false,
  "breadcrumbs.enabled": false,
  "editor.wordWrap": "on"
}
```

---

## Delivery Tips

### Pacing
- **Sections 1–2** (Introduction + Prompting): Move briskly. These build anticipation.
- **Section 3** (Patterns): Medium pace. Each pattern is a mini-demo. Don't over-explain.
- **Section 4** (Pandas): Deliberate pace. This is the core. Narrate your thought process.
- **Section 5** (Lab): Step back. Let attendees drive. Walk the room.
- **Sections 6–7** (Advanced + Wrap): Quick and energizing. End strong.

### Engagement Techniques
- Ask "Who has used Copilot before?" at the start (calibrate your audience)
- After each demo, pause 5 seconds: "Questions on this before we move on?"
- During the pandas scenario, narrate your prompt strategy: "I'm adding constraints because..."
- In the lab, ask advanced users to try stretch goals so they don't get bored
- Use "think-aloud" during demos: verbalize why you're writing each part of the prompt

### Handling Mixed Skill Levels
- **Beginners:** The core content is designed for them. Reassure them that iterating is normal.
- **Intermediate:** The prompt progression and pattern library give them new techniques.
- **Advanced:** The stretch goals and advanced capabilities section are for them. Engage them as helpers during the lab.

---

## Common Pitfalls & Mitigations

| Pitfall | Mitigation |
|---------|-----------|
| Copilot gives different output than rehearsed | Don't panic. Say "Copilot's suggestions vary—let's see what we got and evaluate it." This is actually a teaching moment. |
| Copilot service is slow/down | Switch to backup screenshots. Narrate: "In a live session, this would generate in 2-3 seconds." |
| Attendees can't get Copilot working | Have a co-facilitator help individuals. Don't stop the session for one person. Pair them with a neighbor. |
| Running over time | Cut Section 6 (Advanced) to 2 minutes. Shorten lab debrief. Never cut the lab itself. |
| Running under time | Extend the lab. Take more questions. Show an additional demo from the patterns section. |
| Attendees ask about pricing/licensing | "That's a great question for your GitHub account team. Today we're focused on the developer experience." Redirect gracefully. |
| "Can Copilot do X?" tangent questions | "Great question. Let's try it live!" (if quick) or "That's a great exploration topic—try it in the lab." |
| Code doesn't run due to env issues | Have a pre-run notebook with all outputs visible as backup. Show the code + output as static content if needed. |

---

## Fallback Plan

### If Copilot is completely unavailable:

1. **Don't cancel the session.** The prompting framework and patterns are valuable regardless.
2. Switch to pre-recorded short clips (30-60 seconds each) showing each demo.
3. Use screenshots with annotations showing the prompt → result flow.
4. Convert the hands-on lab into a "prompt writing exercise" (attendees write prompts on paper/doc, discuss as a group).
5. Spend more time on the prompt library walkthrough and group discussion.

### If time runs critically short (< 20 min for remaining content):

Priority order (cut from bottom):
1. ~~Wrap-up~~ → Skip, share slides with habits listed
2. ~~Advanced capabilities~~ → Skip entirely
3. ~~Lab debrief~~ → Skip, let people continue on their own
4. Keep the lab (even if shortened to 5 min)
5. Never cut the pandas scenario—it's the core deliverable

---

## Post-Workshop

- [ ] Share all materials (slides, prompt library, lab, dataset) via agreed channel
- [ ] Send follow-up email with:
  - Link to materials
  - 5 productivity habits summary
  - Recommended next steps
  - Feedback survey link
- [ ] Collect feedback for iteration
- [ ] Note what worked/didn't for the next delivery

---

## Facilitator Self-Assessment

After delivery, rate yourself:
- [ ] Did I stay within 90 minutes?
- [ ] Did all demos work? If not, did I recover smoothly?
- [ ] Did attendees engage during the lab?
- [ ] Did I narrate my prompt strategy (not just type silently)?
- [ ] Did I accommodate different skill levels?
- [ ] Would I change the pacing for next time?
