<!-- Text extraction of "i2ai course project instructions (latest).pdf" (pdftotext -layout). This PDF is NEWER than the .docx version and takes precedence where they differ. Still watermarked "draft" by the instructor. -->

```text
Overview
i2ai Team Project Instructions
Learning Objectives
   ●​ Apply coordination, collaboration and communication skills in a team-based client
      engagement.
   ●​ Gather and analyze client requirements.
   ●​ Critically apply agentic AI skills and tools to solve a real-world problem based on client
      requirements.

Overview
Each team in the Intro to AI course (Fall 2026) at CMU's Heinz College will complete a
semester-long project for a client. This is a low-stakes (no contract, no payment, no legal
obligations) project, NOT a capstone project.

                                          t
A client provides a small and actionable problem for students to address using agentic AI. The
client may or may not provide access to the organization's data. Students may build an app, a

dr
website, or other solutions using simulated data/accounts. The project list and team
assignments are available here.

A client may be assigned one or two student teams. We do so for two reasons:

  af
    1.​ Keep the team size at 5 or less. Teams bigger than 5 become very difficult to
        manage/coordinate.
    2.​ Different teams can approach the same problem from different angles, and the client
        can get two different solutions that they can compare and contrast. The two teams
        can learn new ideas from each other as well (during the final presentations).

Technical Requirements
In addition to meeting client requirements, the project team must demonstrate:
    1.​ How the team has accomplished the project using an agentic workflow, and/or have
        helped the client establish an agentic workflow
    2.​ How a pretrained model (e.g. an LLM, a pretrained prediction/vision model, etc), or a
        model that the team has trained from scratch, is incorporated into the solution
    3.​ At least five agentic tools (with well-written docstring documentation designed for
        LLM agents to read) that the team has custom designed for this project and for an
        LLM-based agent to use and to control the LLM-based agent’s behavior in a more
        deterministic manner
    4.​ A skill folder with a skill.md file and/or templates that the team used for developing
        the solution, or that the team has designed for the client to use in the future
    5.​ Methods that the team has used to evaluate the system’s performance
    6.​ Methods that the team has used to protect client data, or to simulate test data. If you
        simulated data, explain how you ensure the quality of the simulated dataset.
   7.​ Safety guardrails (perhaps as agentic tools from 3., or parts of the skill folder, etc) to
       address potential risks and ethical concerns
          a.​ How the model behaves with vs. without the safety guardrails to illustrate the
              effectiveness of such safety guardrails

Project Privacy & Confidentiality
The nature of the projects and client identity is by default confidential. Some clients may ask
you to sign an NDA. Do NOT discuss project or client identity details without permission.
Always check with the client and get permission before you share details with those outside
the project/TA/instructor. To post about the project on social media (e.g. LinkedIn), send a
draft to your client for approval before posting.

Data Access
Most clients won't be able to share sensitive data with you. You will be responsible to simulate

                af
data for testing as needed.

Intellectual Property

                   t
The intellectual property of this work is shared between the student team and the client.

Client Interaction
Three client meetings are required during the semester:
(1) first client requirements meeting: late September
(2) progress update: early November
(3) final presentation: early December

dr
Deliverables - See syllabus for due dates
Team Project #1: Team Contract and Project Topic Exploration
Team Project #2: Progress update
Team Project #3: Final Deliverable
Team Project #1
Team Project #1: Team Contract & Scope
Purpose
Before you engage a client, your team needs (1) a working agreement on how you'll
collaborate, and (2) a claimed topic/client with an initial understanding of the problem
space.

Part A - Team Contract
Complete the team contract template covering:

   ●​
   ●​
   ●​
   ●​

                af
        Team member contact info, availability, strengths, and areas to watch
        Team norms (meeting cadence, communication, decision-making)
        Expectations and conflict resolution process
        Team goals

                   t
Part B - Client Meeting Prep
   1.​ Review information about the client assigned to your team.
   2.​ Send an initial outreach email to your client (instructions provided in the Appendix) to
       introduce your team and request a kickoff meeting.
   3.​ Research client organization and client information before the client meeting.

dr 4.​ Hold your first client requirements meeting (late September, before Team Project #1
       deliverable is due - see syllabus for the due date). Come prepared to ask about:
           ○​ A specific, actionable problem they'd like addressed
           ○​ Constraints, context, or examples that help scope the problem
           ○​ What data (simulated/public) you'll need, and whether an NDA is required
           ○​ What a successful outcome looks like to them by December
           ○​ A date/time for the progress update meeting: late October or early November
   5.​ Invite the client to attend your final poster presentation (see syllabus for date) -
       discuss in the meeting and follow up with a calendar invite.
           ○​ If your client is remote, schedule a time to present your final deliverables to
               the client.

Part C - Project Scope
Based on the client meeting, write a clear project scope document based on these PMI
instructions. Send the project scope document to your client for approval.
Build a Github kanban board to start managing your project. See here for an example board.
Follow online tutorials like this one.

Submission in Canvas
Three documents:

   1.​ Signed team contract
   2.​ Short (~1 page) client meeting prep document: who the client is (or anonymized
       description if confidentiality requested), the problem as currently understood, and a
       list of questions for the client before heading into the first client meeting.
   3.​ Project scope document (which your client may or may not have approved) with a link
       to your team’s kanban board.

Appendix. Template email to the client

                af
Instructions for teams:

                   t
   1.​ Find out if more than one team is assigned to the same client. All teams assigned to
       the same client should work together with the assigned project TA to identify meeting
       times/dates that work for most people. Include these options in the email to the client
       for the client to select.
            a.​ Note: Even if multiple teams are meeting with the same client, the teams will
                work on the same topic separately. Some clients may give different teams
                different topics, but most will give the same topic to all teams.
   2.​ Fill in the bracketed placeholders, and adjust the tone to fit your client.

dr 3.​ Appoint one person to send the email to the client (copying the TA, instructor, and all
       team members) to schedule your initial requirements meeting.

Subject: Intro & Scheduling — [Team Name] / CMU Intro to AI Project

Hi [Client Name],

My name is [Your Name], and I'm reaching out on behalf of our team(s) — [list team members]
— from Carnegie Mellon University's Heinz College. We're students in the Intro to AI course this
semester with Dr. Rachel Chung as our professor. We've been paired with you as our project
client for a semester-long agentic AI project. Our project will be supported by our TA [TA
name].

This is an academic project, with no contract, payment, or legal obligation on your end. We
won't need access to your organization's actual data or systems, although you are welcome to
provide data or access. We will build our solution using simulated or publicly available data. If
you'd like us to sign an NDA before discussing any details, we're glad to do that.

We'd love to set up a short kickoff call (30 minutes or so) before the end of September to
understand:

   ●​ A specific, actionable problem you'd like us to explore using agentic AI (an AI system
      that can plan and take multi-step actions, not just answer questions)
   ●​ Any context, constraints, or examples that would help us scope the problem well
   ●​ What a useful outcome would look like from your perspective by early December

Would any of the following work for a quick call? [Option 1] / [Option 2] / [Option 3] (Specify
time zone as the client may be in a different time zone.)

(For local clients only) Please let us know if you’d like to meet in person at CMU or your
office, or remotely on Zoom.

                af
Looking forward to working with you this semester.

Best, [Your Name] [Contact info]

                   t
dr
contract
Team Contract — Intro to AI, Fall 2026
Purpose: Before you start your client project, your team needs a shared agreement on how
you'll work together — who's good at what, when you're available, and how you'll handle it if
something goes sideways. This isn't busywork: teams that skip this conversation tend to hit the
same conflicts around week 6 that a 20-minute discussion now would have prevented.

Each team should:

   1.​ Sit together and fill this out collaboratively — don't split it up and stitch it together later.
       The point is the conversation, not the document.
   2.​ Be honest about weaknesses and availability. A contract full of "no weaknesses,
       available anytime" helps no one in week 10.
   3.​ Agree on the norms and conflict resolution sections as a group — these are the parts

                 af
       you'll actually reference if something goes wrong.
   4.​ Submit the completed contract as Team Project #1, alongside your topic selection.

1. Team Info
Team name

                    t
Client / project topic

2. Team Members

dr
Repeat this block for each member.

Name: Email: Phone (optional, for urgent coordination): Availability/commitment:
(recurring conflicts — classes, work, sports — and general flexibility) Strengths: (skills, tools, or
working styles you bring) Areas to watch: (where you might need support or accountability from
teammates — e.g., procrastination, limited coding background, tends to overcommit) Preferred
role(s) on this project: (e.g., client communication, technical build, presentation/design, project
management)

3. Team Norms
Meeting cadence: (how often, what day/time, in-person or virtual) Check-in method: (Slack,
group chat, etc. — and expected response time) Decision-making: (how will the team resolve
disagreements on approach — majority vote, client-facing member decides, escalate to
TA/instructor?) Work distribution: (how will tasks get assigned and tracked — e.g., GitHub
project board)

4. Expectations
What does "doing your share" look like for this team?

Attendance: (what happens if someone misses a meeting or a deadline)

5. Conflict Resolution
If a team member isn't meeting expectations, what's the process before escalating to the
TA/instructor?

At what point do you escalate, and to whom?

6. Team Goals

                af
What does a successful outcome look like for this team, beyond just the grade?

                   t
Signatures / acknowledgment By signing below, each member confirms they've discussed
and agreed to the above.

        Name                Signature             Date

dr      Name

        Name

        Name
                            Signature

                            Signature

                            Signature
                                                  Date

                                                  Date

                                                  Date

        Name                Signature             Date
rubric TP1
TP1 Rubric - Team Contract & Scope
Total: 30 points

TBD

                   af t
dr
Team Project #2
Team Project #2: Progress Update
Purpose
Check in on both the client relationship and the technical build roughly halfway through the
project, catch scope or coordination problems early, and give teams structured feedback
before the final push.

What to Prepare
   1.​ Progress against plan: what you scoped at TP1 vs. where you actually are.
   2.​ Working prototype or partial demo: even an early, rough agentic AI component — this

                af
       isn't the polished final product.
   3.​ Blockers/open questions: technical, client-access, or team-coordination issues you
       need help with.
   4.​ Updated scope (if changed): what shifted since TP1 and why.

                   t
   5.​ Project board snapshot: current state of your GitHub kanban board (done/in
       progress/to-do).

Client Meeting
Present the above to your client in an early-November progress-update meeting. Come away
with explicit confirmation (or correction) of direction for the final stretch.

dr
Submission
   ●​ Short progress report (1-3 pages) covering the five points above
   ●​ Link to current GitHub repo state (code + project board)
rubric TP2
TP2 Rubric - Progress Update
Total: 50 points

      Criteria       Points                      What we're looking for

 Progress vs. plan   10       Honest, specific comparison of TP1 scope to actual progress;
                              meaningful work completed by this point

 Working             12       A functioning (even if rough) agentic AI component — real
 prototype/demo               progress on the actual build, not just planning docs

 Blockers &          8        Blockers are clearly identified with a credible plan to resolve
 problem-solving              them

 Scope updates

 Project board
 upkeep

 Client meeting
 quality
                   af5

                     5

                      t
                     10
                              If scope changed, the reasoning is sound and clearly explained

                              Kanban board reflects real, current task status

                              Client meeting held; team came away with clear, confirmed
                              direction for the remainder of the project

dr
Team Project #3
Team Project #3: Final Deliverable
Purpose
Present a working prototype of an agentic AI application solving your client's problem, hosted
in a complete GitHub repo, to faculty, guests, and students.

Required GitHub Repo Contents
   1.​ README — comprehensive project report addressing all technical requirements given
       in the project overview, including:
           ○​ Visuals illustrating your core concept and its business relevance

                af
           ○​ Author list with links to each member's GitHub profile (with a proper bio)
           ○​ Project scope — as narrowly and specifically defined as possible
           ○​ Project details — clearly organized, concise writeups
           ○​ "What's next?" — future development directions and open concerns

                   t
           ○​ Responsible AI considerations
           ○​ Reference list, including at least one high-quality research paper (not
               news/blog/LinkedIn), published within the last 3 years
           ○​ Do not disclose your client's identity without their permission
   2.​ Runnable demo code — a .py file, Jupyter notebook, or Colab link. Must run live
       during the presentation. Cite any code sourced from elsewhere.
   3.​ Externally hosted app/website — built using GenAI tools with agentic capabilities

dr     (e.g., an agent that plans/acts across steps, not just single-turn Q&A).
   4.​ Project board — kanban-style board (done / in progress / to-do) used throughout the
       semester. Be ready to discuss how your team actually used it.

Presentation Requirements
Be ready to discuss:

   1.​ Problem statement — what you solved and why it matters
   2.​ Research paper — the required paper and how it informed your approach
   3.​ Code demo — keep it simple; illustrate one essential concept rather than the whole
       project
   4.​ Website/app demo — show it live and explain its agentic design
          a.​ Address all of the technical requirements given in the overview
rubric TP3
TP3 Rubric - Final Deliverable
Total: 120

For each rubric: Excellent = 100% ​ Satisfactory = 75%​       Unsatisfactory = 50%​​      Poor = 25%

Criteria                                                                                                              Percentage
                                                                                                                          7%

                                     af
Code demo: Technically challenging, logically sound, and thoughtfully put together.

Website demo: Creative and thoughtful use of vibe coding

                                        t
Poster is visually effective and covers everything that's required for the project.

Github repo is organized and covers everything required for the project effectively.

Github project kanban board is visually organized.

Research paper is well chosen and well discussed verbally and on the poster.
                                                                                                                         7%

                                                                                                                         7%

                                                                                                                         7%

                                                                                                                         7%

                                                                                                                         7%

           dr
References are cited properly.

The team articulated their problem statement, rationale, and overall approach effectively to the judges.

The team articulated the business opportunities and challenges of their project work clearly and effectively to the
judges.

The team explained the technical components of their project clearly and effectively for a non-technical audience.

The team helped the judges learned a significant amount of new knowledge about AI.
                                                                                                                         7%

                                                                                                                         9%

                                                                                                                         9%

                                                                                                                         12%

                                                                                                                         7%
                                                                                                                7%
The team demonstrated creativity in their approach to their project topic.

The team demonstrates effective team collaboration with all team members actively engaged in presentation and   7%
Q&A.

                                    af t
        dr
```
