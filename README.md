# Notes on Software Engineering

This repository contains a collection of notes and lessons learned that I have
gathered over time during my work as a software engineer.

These notes are not strict instructions to be followed; rather, they serve as
soft guidelines and recommendations. They are most valuable when considered as a
whole. Taken individually, some notes may even appear to contradict one another.
Following them too rigidly can diminish their usefulness or, in some cases, lead
to negative outcomes. There may also be some overlap between notes, so it's
important not to interpret them too literally.

Most of the notes are my own observations, though I occasionally quote from
influential books and other resources. All notes with quotations include
references to their sources.

This repository is currently a draft, far from complete, and organized
arbitrarily. Please do not expect it to be polished.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Day-to-Day Work](#day-to-day-work)
  - [Leave Work Better](#leave-work-better)
  - [Fast Feedback](#fast-feedback)
  - [Start Simple](#start-simple)
  - [Break Down Work](#break-down-work)
  - [Look Outside Your Immediate Task, Maintain the Bigger Picture](#look-outside-your-immediate-task-maintain-the-bigger-picture)
  - [Avoid Work That Can Be Avoided](#avoid-work-that-can-be-avoided)
  - [Understand and Respect the Customer](#understand-and-respect-the-customer)
  - [Choose Where to Innovate (Carefully)](#choose-where-to-innovate-carefully)
  - [Automate everything](#automate-everything)
  - [Quick exploration](#quick-exploration)
  - [Stay Curious and Explore](#stay-curious-and-explore)
  - [Task Sequencing: Group Related Activities for Efficiency](#task-sequencing-group-related-activities-for-efficiency)
  - [Plant the Tasks, Let the Mind Work](#plant-the-tasks-let-the-mind-work)
  - [Strive for Clarity](#strive-for-clarity)
  - [Provide your communication with clear evidence](#provide-your-communication-with-clear-evidence)
  - [Exercise sound judgment](#exercise-sound-judgment)
  - [Be Prepared](#be-prepared)
  - [Everything Explicit. No Magic.](#everything-explicit-no-magic)
  - [Disown Your Work by Sharing It with the Team](#disown-your-work-by-sharing-it-with-the-team)
  - [Learn from Lessons](#learn-from-lessons)
  - [Use Diagrams](#use-diagrams)
- [Teamwork and Communication](#teamwork-and-communication)
  - [Agile Software Development Requires Strong Social Network](#agile-software-development-requires-strong-social-network)
  - [Sending Status Updates to the Team](#sending-status-updates-to-the-team)
  - [Close the loops, acknowledge communication, always follow up](#close-the-loops-acknowledge-communication-always-follow-up)
  - [Use Structure-Preserving Responses](#use-structure-preserving-responses)
  - [Keep Everyone in the Loop](#keep-everyone-in-the-loop)
  - [Leverage Early Expert Review and Broad Feedback](#leverage-early-expert-review-and-broad-feedback)
  - [Talk in Person When You Can](#talk-in-person-when-you-can)
  - [Recognize the ideas and achievements of your colleagues](#recognize-the-ideas-and-achievements-of-your-colleagues)
  - [Praise Good Work](#praise-good-work)
  - [Professional content](#professional-content)
  - [Loop in Experts for Important Actions](#loop-in-experts-for-important-actions)
  - [Share What Works](#share-what-works)
  - [Share and Improve Team Workflows](#share-and-improve-team-workflows)
  - [Keep Team Knowledge Alive](#keep-team-knowledge-alive)
  - [Create a Superset of Conflicting Interests or Clarify the Problem](#create-a-superset-of-conflicting-interests-or-clarify-the-problem)
- [Complexity and Cognitive Load](#complexity-and-cognitive-load)
  - [Solving Right Problems](#solving-right-problems)
  - [Solutions are Context-Driven](#solutions-are-context-driven)
  - [Evolution from Local Optimum to Better Optimum](#evolution-from-local-optimum-to-better-optimum)
  - [Weakest link](#weakest-link)
  - [Point of View](#point-of-view)
  - [Periphery](#periphery)
  - [Rational and Unconscious](#rational-and-unconscious)
  - [Engineering as Input/Output: The Role of Prepared Inputs](#engineering-as-inputoutput-the-role-of-prepared-inputs)
  - [Humans are not designed for Big Numbers](#humans-are-not-designed-for-big-numbers)
  - [There is no such thing as Many](#there-is-no-such-thing-as-many)
  - [0-1-2-Many I](#0-1-2-many-i)
  - [0-1-2-Many II](#0-1-2-many-ii)
  - [Masking (Shadowing)](#masking-shadowing)
  - [Weighting system](#weighting-system)
- [Design](#design)
  - [Functional analysis and decomposition](#functional-analysis-and-decomposition)
  - [Poor Abstraction](#poor-abstraction)
  - [Cost of Abstraction](#cost-of-abstraction)
  - [Habitability](#habitability)
  - [Hard Things](#hard-things)
  - [True Name](#true-name)
  - [One Pattern per Class](#one-pattern-per-class)
  - [Archetype](#archetype)
  - [Prima Materia](#prima-materia)
  - [Mature automation](#mature-automation)
  - ["Magic" is automation that is not adequate](#magic-is-automation-that-is-not-adequate)
  - [Poisonous Systems](#poisonous-systems)
  - [Bad Design in House](#bad-design-in-house)
  - [Unnecessary Flexibility](#unnecessary-flexibility)
  - [Black Box with a Green Play Button](#black-box-with-a-green-play-button)
  - [Single Source Concept and Its Exceptions](#single-source-concept-and-its-exceptions)
  - [Resilience to Change vs Fixed Perfect Solutions](#resilience-to-change-vs-fixed-perfect-solutions)
  - [Two Almost Identical Entities](#two-almost-identical-entities)
  - [Design for Operations](#design-for-operations)
  - [Control](#control)
    - [Observable Control](#observable-control)
    - [Humans should dominate machines](#humans-should-dominate-machines)
    - [Overlapping control](#overlapping-control)
    - [Broken control loops](#broken-control-loops)
  - [Feedback](#feedback)
    - [Broken feedback loops](#broken-feedback-loops)
  - [Separation / partitioning](#separation--partitioning)
  - [Trade-off of Encapsulation](#trade-off-of-encapsulation)
  - [Grouping](#grouping)
  - [Observability vs Correctness](#observability-vs-correctness)
  - [Don't Use RAII on a Business Logic Level](#dont-use-raii-on-a-business-logic-level)
  - [Rich Collection of Models and Diagrams](#rich-collection-of-models-and-diagrams)
  - [The Limits and Choices of Models and Diagrams](#the-limits-and-choices-of-models-and-diagrams)
  - [Pseudocode as a Modeling Tool](#pseudocode-as-a-modeling-tool)
- [Coding, code reviews, and maintenance programming](#coding-code-reviews-and-maintenance-programming)
  - [Code that Works](#code-that-works)
  - [Code Is Not Your Partner](#code-is-not-your-partner)
  - [Two Strategies for Replacing a Feature](#two-strategies-for-replacing-a-feature)
  - [Smallest Scope](#smallest-scope)
  - [Code Style as a Blocker](#code-style-as-a-blocker)
  - [Avoid Plural Names For Classes](#avoid-plural-names-for-classes)
  - [Fast Programming and Slow Programming](#fast-programming-and-slow-programming)
  - [Stable Components](#stable-components)
  - [Boring Code](#boring-code)
  - [Boring Code 2](#boring-code-2)
  - [Lack of Knowledge](#lack-of-knowledge)
  - [Lack of Knowledge II](#lack-of-knowledge-ii)
  - [Goodwill vs Pain](#goodwill-vs-pain)
- [Version control, Git, code reviews](#version-control-git-code-reviews)
  - [Simplifying Complex Feature Branches](#simplifying-complex-feature-branches)
  - [The Moving and Changing Anti-pattern](#the-moving-and-changing-anti-pattern)
  - [Git commit names: Context: Title](#git-commit-names-context-title)
- [Biases](#biases)
  - [If It Works, Then It Works Bias](#if-it-works-then-it-works-bias)
  - [Focusing only on what's most visible bias](#focusing-only-on-whats-most-visible-bias)
  - [The Fix Bias](#the-fix-bias)
  - [Resolving Merge Conflict Bias](#resolving-merge-conflict-bias)
- [Reliability](#reliability)
  - [Errors are not ok](#errors-are-not-ok)
  - [Errors must be understood and described](#errors-must-be-understood-and-described)
  - [Underlying errors shall not be hidden](#underlying-errors-shall-not-be-hidden)
  - [Critical errors vs non-critical errors](#critical-errors-vs-non-critical-errors)
  - [Assertions are better than no error handling](#assertions-are-better-than-no-error-handling)
  - [Assertions are shortcuts for a proper error handling](#assertions-are-shortcuts-for-a-proper-error-handling)
  - [Crash Early](#crash-early)
- [Testing](#testing)
  - [Write Tests, Even Bad Ones](#write-tests-even-bad-ones)
  - [TDD as a Toolbox](#tdd-as-a-toolbox)
  - [Legacy Code is Code Without Tests](#legacy-code-is-code-without-tests)
  - [Testing as a Way to Manage Complexity](#testing-as-a-way-to-manage-complexity)
  - [Test It to Engineer It](#test-it-to-engineer-it)
  - [Improve Testability](#improve-testability)
  - [Getting the first test to work](#getting-the-first-test-to-work)
  - [What to Test](#what-to-test)
- [Distribution](#distribution)
  - [Provide Basic Test Sequences with Your Product](#provide-basic-test-sequences-with-your-product)
  - [Provide Drivers Alongside Your Hardware](#provide-drivers-alongside-your-hardware)
  - [Provide Simulators Alongside Your Hardware](#provide-simulators-alongside-your-hardware)
- [Documentation](#documentation)
  - [The Illusion of Easy Documentation](#the-illusion-of-easy-documentation)
  - [Software Design Document](#software-design-document)
  - [Less prose, more structure](#less-prose-more-structure)
  - [Too Much Structure Overload](#too-much-structure-overload)
  - [Encyclopedic Document](#encyclopedic-document)
- [Meetings](#meetings)
  - [Sound Check](#sound-check)
  - [Meeting Agenda](#meeting-agenda)
  - [Meeting Notes](#meeting-notes)
  - [Capturing Meeting Results](#capturing-meeting-results)
  - [Briefing In](#briefing-in)
  - [Briefing out](#briefing-out)
  - [Sharing Screen & Presenting Material](#sharing-screen--presenting-material)
- [Systems](#systems)
  - [Good enough is often best](#good-enough-is-often-best)
  - [Designing Systems for Effective Work](#designing-systems-for-effective-work)
  - [The Risk of Default Outcomes](#the-risk-of-default-outcomes)
- [People and Organizations](#people-and-organizations)
  - [Everyone is busy](#everyone-is-busy)
  - [Solving Problems with Cash](#solving-problems-with-cash)
  - [The Paradox of Rushing in Software/Systems Engineering](#the-paradox-of-rushing-in-softwaresystems-engineering)
  - [Four seasons](#four-seasons)
- [Standards](#standards)
  - [Idealized standards vs. practical implementation](#idealized-standards-vs-practical-implementation)
  - [The challenge of standards implementation](#the-challenge-of-standards-implementation)
  - [Standards and best practices](#standards-and-best-practices)
  - [Standards favor good practice](#standards-favor-good-practice)
  - [Wrong is worse than early or incomplete](#wrong-is-worse-than-early-or-incomplete)
  - [Standards vs Hardcoded Implementations](#standards-vs-hardcoded-implementations)
- [Requirements](#requirements)
  - [One-stop shopping](#one-stop-shopping)
- [Safety](#safety)
  - [Safety does not exist without blood, loss or failure](#safety-does-not-exist-without-blood-loss-or-failure)
  - [Safety is boring](#safety-is-boring)
  - [Safety is very hard to achieve but is very easy to lose](#safety-is-very-hard-to-achieve-but-is-very-easy-to-lose)
  - [Success breeds failure](#success-breeds-failure)
  - [Safety as a Defensive Discipline](#safety-as-a-defensive-discipline)
  - [Safety for Engineering is Like Medicine for People](#safety-for-engineering-is-like-medicine-for-people)
  - [Understanding as a Prerequisite for Safety Assessment](#understanding-as-a-prerequisite-for-safety-assessment)
  - [User Interfaces and Critical Systems](#user-interfaces-and-critical-systems)
- [Books](#books)
- [Similar resources](#similar-resources)
- [Copyright](#copyright)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Day-to-Day Work

### Leave Work Better

Always leave the work artifacts - whether code, documentation, diagrams, models,
or others - in a better state than they were before, giving future you or
someone else the opportunity to improve them even further.

### Fast Feedback

Fast feedback is essential for making progress and avoiding wasted effort. It
helps engineers quickly test ideas, catch mistakes early, and stay in the flow.
Useful ways to get fast feedback include test-driven development, fast-running
test suites, effective debugging tools, and simply asking a colleague for quick
advice. When starting on a new project, one of the first things to learn is how
to run the existing tests, write new ones, and figure out the quickest way to
debug. Investing in faster tools, clearer error messages, and smoother processes
pays off - the shorter the feedback loop, the more confidently and efficiently
you can work.

### Start Simple

Start with something simple, then extend it further. Most often a complex
problem is a composition of simpler problems. If you are facing a problem and
you are afraid of the complexity it exerts, try to make a smallest possible step
towards the solution and see what you can do from there. Simple can also mean
quick and dirty but that's ok as that's only a start. Once you have something
simple working you have a ground to move on further. Most likely this means you
have an **archetype** of a future thing, real and complex system.

See also Kent Beck's
[Test-Driven Development book](https://en.wikipedia.org/wiki/Test-Driven_Development_by_Example)
where this approach of doing simple things is explained at great depth.

### Break Down Work

Divide complex tasks into smaller subtasks. Keep breaking them down until each
subtask is short and manageable. This helps with detailed planning and assigning
work to the right people.

Align task breakdown with the technical architecture and vice versa. Ideally,
work packages, epics, or tasks correspond to functional components. This way,
working on a task means focusing on a single component or closely related parts.
Design the architecture so that work naturally fits its components.

For splitting software components, see Separation / Partitioning. Also, check
Point of View for more context.

### Look Outside Your Immediate Task, Maintain the Bigger Picture

When starting any task, take time to understand the rationale behind it (the
WHY). See how the task connects to broader goals, milestones, or parallel
efforts. It may be part of a chain where upstream or downstream effects matter.

Maintain awareness of the bigger picture. A task that seems minor may be a
critical blocker for a more visible effort. Conversely, something that appears
simple might turn out to be time-consuming and affect teammates or dependencies.

With a deep understanding of the task, you will start seeing how different
strategies (e.g., Strategy X vs. Strategy Y) can lead to different outcomes.
This kind of insight allows you to:

- Escalate risks early.
- Spot opportunities.
- Align better with the system's or team's needs.

A practical application of this mindset in documentation writing: start each
technical page with a clear problem statement and a description of its
surrounding context.

- Who or what benefits if this task is completed?
- Does it enable a system, a process, or a team?
- What is the strategic value of solving it?

Framing the problem this way helps readers, especially future engineers, orient
themselves and understand the significance of the solution that follows.

### Avoid Work That Can Be Avoided

Before starting or planning any work, always ask: Is this work truly necessary?

Sometimes, tasks are initiated based on uninformed decisions, leading to work
that ultimately provides little value or fails to achieve the desired outcomes.

"Busy work" refers to inefficient tasks that consume time and resources while
contributing little to the project's success. It can compromise schedules,
reduce technical consistency, lower team morale, and create the illusion of
progress. The ability to recognize and eliminate busy work is one of the skills
that distinguishes a senior engineer from a junior one.

Engineering is sometimes cheating. Instead of implementing something
sophisticated, a smarter workaround can achieve the same result with far less
effort. For example, rather than building a solution from scratch, reuse
existing work - whether by leveraging open-source software or buying an
off-the-shelf system.

In software development, there's a well-known saying: "The best code is the code
that is never written".

### Understand and Respect the Customer

Take time to deeply understand and respect the customer, both the people and the
domain they operate in. Immerse yourself in their context. Know what they care
about, what problems they face, and how your work fits into their world.

When things go smoothly, this understanding helps you deliver real value. When
things get challenging, such as when delays or technical setbacks arise, this
relationship matters even more.

In such situations, transparency is better than defensiveness. A clear and
honest update, even when delivering bad news, builds trust. Customers almost
always prefer being informed early over being surprised later. A transparent
explanation of issues, trade-offs, and risks shows respect for their time,
planning, and decision-making.

### Choose Where to Innovate (Carefully)

Innovate where your business's focus lies and stay conservative with other areas
by using established technologies.

For example, a company focused on rocket software should likely avoid building
its own web framework or NoSQL database. Exceptions exist, but they are rare,
especially when a company diversifies into a highly successful product unrelated
to its core business. Innovating in too many areas can compromise the core
product and cause missed deadlines.

For a great explanation, refer to this
[Boring Technology presentation](https://boringtechnology.club/).

### Automate everything

Seek opportunities to automate processes or tasks. Automation eliminates busy
work, freeing time for more valuable activities. It reduces human error,
increases efficiency, and helps to maintain consistency. The best workflows are
automated ones.

### Quick exploration

The solution you're looking for might be just two clicks and a couple of Google
searches away.

When reading large documents, it can be helpful to "fly over" them to quickly
locate the most relevant section rather than reading from A to Z.

When exploring with code, a combination of quick-and-dirty scripts can sometimes
create miracles, giving immediate and valuable insights. Instead of discarding
an idea because it's complex and time-consuming, try implementing a very basic
version first because it might provide useful insights or even a functional
solution right away.

### Stay Curious and Explore

Look around and see what is new in your field. If you find a cool project, check
who made it and what else they have done. Go to conferences and events. Being
curious helps you learn new things, meet new people, and get fresh ideas.

### Task Sequencing: Group Related Activities for Efficiency

When sequencing tasks (especially repetitive ones), group related tasks together
and separate them from others.

One useful pattern is the 'Inbox' approach, where input is first collected and
then executed upon. For example, when writing a technical document, split the
task of gathering the document content (the 'Inbox' with bullet points) from the
task of formulating and spelling out each individual content item.

### Plant the Tasks, Let the Mind Work

When you are overloaded with several non-trivial tasks, try starting all of them
by just 10-20%, then switch between them. The goal is to build an initial
understanding for each task and give your mind time to work on them in the
background (what people often call "sleeping on it").

The subconscious is an interesting mechanism: when given a few active problems
to process, it starts building structure around them even when you are not
focused on them directly. Later, continuing from that 10-20% starting point
often feels much easier. The process can be repeated from 10-20% to 30-40% to
50-60% and so on.

This approach also helps with communication: once you've started a task, you're
already in a position to ask questions, clarify assumptions, or unblock others
who depend on your output.

### Strive for Clarity

Strive for clarity in everything you do. Put in the effort to make the products
of your work, or the aspects of the system you're working on, as clear as
possible. Simplify complexity - either by reducing the complexity itself through
development or, if that's not feasible, by explaining the details as clearly as
possible.

Avoid owning too many non-obvious details about your work that only you
understand. Do not hold onto esoteric knowledge - de-esoterize it. Document it
for everyone to access.

Encyclopedism or esotericism is an anti-pattern because it obscures common
knowledge about the system for others.

- Document everything, especially the most complex topics.
- Use plain English and diagrams to explain complex topics to your colleagues.
  Test your content with them to ensure it is accessible. If it's still unclear,
  ask for their feedback to improve it.

### Provide your communication with clear evidence

When you share your own work or thoughts, or the work or thoughts of others,
make it short and easy to understand. Add clear and simple visual materials or
examples.

Whenever you can, include diagrams, screenshots, code blocks, logs, or similar
items. These give direct proof and make your message clear.

For every message you send, try to give the clearest evidence. This helps the
receiver understand you right away, without extra effort.

### Exercise sound judgment

Learn to recognize when an established pattern or guideline should be followed
and when it should not. Apply rules with sensitivity to context and priorities
instead of treating them as absolute. Be ready to make calls in situations where
existing rules or processes do not yet provide clear guidance, which often
happens with new technologies, new problems, or unfamiliar constraints. Accept
that difficult situations sometimes require clearly saying YES or NO, or
deliberately making an exception to a rule, policy, or established practice.

Use sound judgment in concrete situations such as deciding whether to follow a
coding guideline strictly or make a justified exception, whether to adopt or
retire a technology, create or dissolve a team, prioritize an initiative, or
stop work that is no longer proving effective. At the same time, recognize the
limits of your own knowledge. What may look like an outdated or incomplete
policy can also be a sign of missing context or insufficient understanding. In
such cases, a better decision may be to learn more about the standard or policy,
understand the rationale behind it, or gather additional information before
acting. Sound judgment develops through experience and reflection and requires a
certain amount of personal courage.

### Be Prepared

Anticipate and prepare for tasks in advance. The famous principle "be prepared"
applies to software engineering just as it does to any other field. Prepare and
script in advance everything that can be anticipated - this allows you to
deliver with high efficiency, good timing, and a positive atmosphere during and
after the activity.

Plan your work week ahead of time. Think through work items before starting
because this makes the week flow more smoothly. Prepare meetings carefully to
make them more productive. Organize workshops, reviews, and other business
events in advance to ensure they proceed efficiently and achieve their goals.

Precompile and structure training materials to make trainings and demonstrations
more effective. Prepare conference presentations thoroughly to deliver them
confidently and clearly.

Ensure that participants receive well-prepared content. When preparation is done
properly, everything appears seamless, easy, and concise. Avoid insufficient
preparation, which leads to confusion, inefficiency, and a poor impression.

### Everything Explicit. No Magic.

Whenever you face a choice between explicit and magic, always choose explicit.

"Magic" is a term software engineers use for anything that is non-obvious,
hidden, overly complex, or no longer suited to the system's current state.

Making things explicit requires a constant effort to ensure clarity, so that
others can understand your work without extra effort. A good test for
explicitness is whether understanding is immediate, with no mental effort or
blockers when going through the material.

### Disown Your Work by Sharing It with the Team

Don't make yourself a bottleneck. If you know something complex, share it,
explain it to the team, document it, or build it into tools and processes. The
goal is to avoid being the only person who understands or owns a specific area.
When knowledge is shared, the team becomes stronger and more resilient.

This doesn't mean giving up ownership. You can still lead and take full
responsibility for a topic. But the results, details, and usage instructions
should be part of the team's shared knowledge. Strong ownership and open
knowledge go hand in hand.

### Learn from Lessons

Do something, then learn from experience. Don't forget - take deliberate time to
reflect. The industry has developed several best practices for capturing lessons
learned:

- Standards: Organizational and industry knowledge is captured in standards,
  handbooks, guidelines, and best practices.
- Post-mortems: When something goes wrong, those involved produce a structured
  report about the event. Larger companies maintain databases of critical
  incidents that employees can study to educate themselves.
- Debriefs: After a meeting, the group discusses what went well or wrong.
- Lessons learned documentation and meetings: After completing an important
  activity, such as a project or milestone, the team takes time to reflect on
  what went well or wrong, learn from it, and document the findings.

Learning doesn't have to be only organizational - it can also be personal.

Examples:

- If a project was successful, what made it so? If a project failed, what were
  the key contributing factors? How can it be improved next time?
- Learning how to estimate software work better - what if a task was estimated
  to take X weeks but actually took 3X? Wouldn't it be valuable to improve
  estimation skills?
- If one colleague is significantly more effective than another, what makes them
  so? What tools, techniques, or habits contribute to their efficiency? Can
  something be learned from them?
- Observing bugs missed during code reviews - what types of bugs tend to escape
  static analysis or peer review? What patterns can be identified to prevent
  them in the future?

### Use Diagrams

Use diagrams as part of your daily work. A diagram can often explain far more
than several paragraphs of text.

Use diagrams for:

- Prototyping and documenting software
- Pair programming
- Hardware-software integration testing
- Meetings (including external meetings)
- Onboarding colleagues
- Everything else where a good visualization helps

There are standards and conventions for creating diagrams, such as UML, but in
practice, even very basic diagrams can be incredibly useful. Use simple shapes
like rectangles and arrows, avoid excessive colors or different shapes, and
express your concepts with the fewest visual elements possible. Creating
diagrams that are too visually complex hinders understanding and reduces their
effectiveness.

## Teamwork and Communication

### Agile Software Development Requires Strong Social Network

**Agile Software Development Requires Strong Social Network**. This statement is
a generalization: This idea has been there from the beginning and since the
inception of the [Agile Manifesto](https://agilemanifesto.org/), but the
following quote from Kent Beck helps to pinpoint it very clearly:

> In The Forest (more specifically on an XP-style team), we handle communication
> of design & implementation multiple ways:
>
> - Communicative code.
> - Readable & predictive tests.
> - A strong social network.
>
> It's only when there is a large audience for stable information (such as the
> JUnit API) that we resort to separate documentation.

See
[Kent Beck - Anatomy of Oscillation](https://tidyfirst.substack.com/p/anatomy-of-oscillation).

### Sending Status Updates to the Team

Software engineering teams often communicate daily via chat. A proven pattern is
for each team member to send updates about their work, allowing the entire team
to see these messages.

Examples of such messages include:

- "Task X is done, here's the PR link. @A and @B, could you take a look?"
- "This week my focus is... Next, I am going to work on..."
- "I see your PR, but I'm working on something else."
- "What does the team think about introducing the coding convention ABC?"

While this may seem obvious for some teams, there are others where daily chats
are completely silent, reflecting a lack of communication between peers
throughout the day. When messages are exchanged, it creates a certain "pulse"
within the team, signaling that the group is actively working on meaningful
tasks and is open to discussion, iteration, and improvement.

This activity not only serves an informational purpose (increasing awareness)
but also has learning, motivational, and even entertaining aspects.

### Close the loops, acknowledge communication, always follow up

A "loop" refers to any situation where one action is followed by another that
resolves the first action in some way. Often, these loops are explicitly called
"feedback loops" because they are closed with feedback that resolves an
outstanding action or state, such as marking it Done, OK, ACK, or something
similar.

Loops can exist in both developed systems and producing organizations.

Examples of loops:

- Answering an email from an existing email thread closes the loop created by
  that thread.
- Closing a Pull Request finalizes its status, either as Done or Won't do.
- Closing a work item ticket to Done.

A task manager is an excellent tool for tracking work items that need to be
completed and closed. For tracking non-trivial project development topics and
trade-offs, a useful practice is to maintain an "Open Questions Log" - a table
where each unresolved or unclosed item is tracked by its current status until it
is resolved.

Sometimes a loop may never be closed, or it may be closed with a significant
delay. Both scenarios can lead to potential problems or even hazards, depending
on the type of system being developed.

Note that 'Won't-do' is also a valid way to close the loop. For example, closing
a Jira ticket with "Won't do" or "Won't fix" positively acknowledges that this
work will no longer linger in someone's backlog.

Not closing loops is often bad practice. Some examples include:

- Not answering an email can cause project delays or result in the
  implementation of a broken or inconsistent system, leading to incidents or
  accidents in the future.
- A missed or forgotten chat message may mean important information is never
  delivered to a critical person.
- A manager neglecting to follow up on an important topic raised by employees,
  leaving it unresolved in an inbox without due attention.

### Use Structure-Preserving Responses

Respond to customer, colleague, or stakeholder input by mirroring it one-to-one.
Keep the same structure, order, and emphasis. If a message contains five points,
respond to all five points in the same order. Treat every point as important and
intentional. Do not assume that understanding is clear. Show understanding
explicitly. This is not politeness. It is proof of understanding.

Avoid the anti-pattern of selective response. Do not answer only one point and
ignore the others. For example, if a message contains points 1a, 1b, 2, 3a, and
3b, do not respond only to 3a. Such responses leave the communication
incomplete. They create false agreement and hide misunderstanding. Problems then
appear later, when they are harder and more expensive to fix.

Apply this discipline not only to written requirements, but also to emails,
workshops, and formal reviews. Use structure-preserving responses to make
understanding visible and reviewable. By respecting the structure of the
message, show that you did not only read the words, but fully understood the
sender's thinking.

### Keep Everyone in the Loop

Share regular updates with the people who rely on your work: your manager,
teammates, or anyone following your technical progress. In fast-moving projects,
keeping others informed helps avoid surprises and keeps everyone aligned.

In an office setting, updates often happen naturally. If the team is
well-connected, these updates may happen through casual conversations or small
talk over lunch. This kind of informal communication spreads useful information
without needing formal meetings.

One big advantage: by the time your work reaches a review-like a code review,
documentation review, or a project milestone-people will already know about it
and may have given input earlier. This makes reviews faster, smoother, and less
stressful.

Another reason to talk about your work: visibility and recognition. Others might
not know:

- what challenges you re facing
- how long something might take
- how your work connects to theirs.

Your teammates are often busy with their own tasks. Clear communication helps
them understand what you are doing and helps your work get noticed and
appreciated.

Stay connected. Stay aligned.

### Leverage Early Expert Review and Broad Feedback

Arrange work so that it passes through the eyes of multiple experts, for
example, through code reviews, design reviews, or walkthroughs. Share proposals
widely to gather diverse perspectives. This approach increases the likelihood of
spotting issues early and improving the overall quality of the work.

Especially during the conception phase, share ideas early before anything is set
in stone. Late feedback can either require costly rework or discourage reviewers
from commenting at all, reducing the benefit of expert input.

See also [Cunningham's Law](https://meta.wikimedia.org/wiki/Cunningham%27s_Law):
"The best way to get the right answer on the internet is not to ask a question;
it's to post the wrong answer."

### Talk in Person When You Can

If something takes a lot to explain, talk in person instead of writing a long
message. It is especially odd when people in the same office email each other
about things they could easily discuss face to face. Quick conversations often
save time and help avoid misunderstandings.

Sometimes, in-person chats mean interrupting someone, and that can be tricky,
especially if they are doing deep work. But often, if the topic involves both
people and can be resolved quickly, a short conversation is worth the
interruption and lets everyone get back to work with better clarity.

### Recognize the ideas and achievements of your colleagues

Teamwork involves contributions from all team members. Whether you are a leader
or an individual contributor, it is essential to give credit where it's due when
expressing an idea that you know was authored by someone else.

This is a good practice because it fosters trust and respect within the team,
encouraging open collaboration and the free exchange of ideas. Recognizing
others' contributions also boosts morale, motivates continued input, and
strengthens the overall effectiveness of the team.

An anti-pattern is when the names of the original authors are omitted, and the
work is presented in the first person, either intentionally or unintentionally,
as if the content were one's own.

### Praise Good Work

Don't hold back from saying "this is great" when a teammate does something
impressive or puts in clear effort. This is especially important if you
consistently deliver high-quality work and expect the same from others. You
might give little feedback because excellence feels like the default. But even a
simple "I see what you have done" can make a real difference. It shows their
work is noticed and appreciated, and it helps build trust and connection within
the team.

### Professional content

When writing an email or chat message, even if addressed to a select group,
consider composing it in a way that it would remain professional and consistent
if shared with a larger or unintended audience. Avoid using vague references
like "we" and "they", especially when referring to internal teams or external
parties such as customers. Refrain from using negative sentences or excessive
emotion. Your content should be polished and ready to be forwarded by anyone, at
any time, whether intentionally or unintentionally.

### Loop in Experts for Important Actions

When making an important decision, involve the right experts. It is better to
include too many people than to miss someone who should have been part of the
process. This practice is especially important when critical decisions with
far-reaching consequences are to be made.

If you are writing an email or message that speaks for your team or group, check
it with others first. Make sure the message reflects what everyone agrees on.

When a message is aligned like this, it:

- Stays strong even if people question it.
- Builds trust inside and outside the team.
- Shows that the team is working together.

Taking the time to check with others makes your message clearer and more
powerful in the long run.

### Share What Works

When something works well for you, don't keep it to yourself and share it with
your team. Everyone has their own way of doing things, but your helpful habit or
method might also work for others. A small improvement shared across a team can
have a big impact.

It is not always obvious what counts as a best practice. But if your approach
makes things easier or more effective, and it is different from how others work,
that could be a sign it is worth sharing or at least suggesting.

### Share and Improve Team Workflows

Try to make daily workflows something the whole team can share. Instead of
everyone using their own custom scripts, set up a common, flexible system for
tasking, development, testing, and debugging. Tools that are used and improved
by many people evolve faster, and the whole team becomes more productive.

### Keep Team Knowledge Alive

Team knowledge and culture can fade over time, just like a person's memory.
Important ways of working and shared values will not last unless they are
repeated and practiced regularly. If not, they slowly disappear from the group's
habits.

To keep them alive, teams need to refresh what matters. Say the important things
often. Practice them together. Repeating is not just a reminder, it is how a
team holds on to what makes it strong.

### Create a Superset of Conflicting Interests or Clarify the Problem

In technical teamwork, it is often the case that if a way forward is clear,
everyone agrees quickly and progress follows naturally. When there is no
agreement, however, discussions can become heated and even personal for those
involved.

In such situations, it is often worth taking a step back to reflect on the
underlying forces at play when a quick solution cannot be found. Pausing helps
reduce friction and personal antipathy, signals that a real problem exists, and
allows the team to clarify all viewpoints and construct a superset of the
conflicting interests.

If this superset is clear and a solution can be found within it, the team can
move forward together. If the superset reveals truly conflicting goals, then
those goals must be refined, agreed upon, or sacrificed.

In any case, once the conflict is clearly defined, there should be fewer hard
feelings, even if the final solution does not reflect every participant's
perspective.

## Complexity and Cognitive Load

> "Complexity can be defined as intellectual unmanageability" (Nancy Leveson,
> Engineering a Safer World, p.4)

https://en.wikipedia.org/wiki/Cognitive_load (and Cognitive Overload)

### Solving Right Problems

"Engineers are great at solving problems but they are not always great at
identifying the right problems to be solved" (Dr. John Thomas, ESWC 2019).

### Solutions are Context-Driven

Even the best solution to a problem is valid only within a given context. A
slight change in the context can invalidate the solution, requiring one to start
from scratch. This understanding highlights that no solution is universally
perfect. Instead, solutions address specific problems or contexts in an "optimal
enough" way. It also encourages detachment from ego-driven perfection, allowing
solutions to evolve as the environment changes.

Examples:

- A clean architecture or pattern may shift to a completely different, sometimes
  opposite, solution due to changing requirements or system environments.
- A "perfect" solution might be discarded because a new team or team leader
  dislikes technology X and prefers technology Y, or simply because it aligns
  with emerging industry trends.
- Perfectly clean code may be rewritten and become more obfuscated due to
  necessary performance optimizations.
- Highly efficient code might be rewritten to sacrifice performance in favor of
  better maintainability and readability, especially for a larger team.

### Evolution from Local Optimum to Better Optimum

Moving from a local optimum to a better solution is often not obvious. When we
are stuck with a solution that is not the best, it can be hard to see better
options. Sometimes a better solution is ignored because it has a cost that seems
too high or because it lacks some aspects of our familiar "good old" solution,
which we are reluctant to give up. But real improvements always have a cost, and
what seems expensive at first can be worth it - it can even change the game.
Sometimes a superior solution comes from areas or techniques that do not seem
"clean" or "organized", yet the final result ends up much better than the
previous one.

A solution that works "well enough" can stop a team from exploring new ideas.
New options are often ignored or not even considered simply because the existing
solution is already in place. At the same time, the current solution can carry
hidden problems that slowly create frustration. Eventually, a new solution may
appear, replacing the old one. It brings its own advantages and disadvantages,
but it works at a higher, more advanced level.

This is where team diversity plays an important role. Fresh perspectives come
from having a variety of viewpoints. If the team is strongly attached to a
locally optimal solution X, but a colleague has experience with an alternative
solution Y, they can help the team step back and consider alternatives in a less
biased way.

### Weakest link

A piece of information is only as clear as its most ambiguous piece. This is a
generalisation from the following fragment from "Patterns for Writing Effective
Use Cases" by Steve Adolph et al., Chapter 6.6:

> Like the old proverb, "A chain is only as strong as its weakest link", a use
> case is only as clear as its most ambiguous step.

### Point of View

[How NASA Builds Teams](https://www.wiley.com/en-us/How+NASA+Builds+Teams%3A+Mission+Critical+Soft+Skills+for+Scientists%2C+Engineers%2C+and+Project+Teams-p-9780470456484):

> The right coordinate system can turn an impossible problem into two really
> hard ones.

[The Early History Of Smalltalk](https://worrydream.com/EarlyHistoryOfSmalltalk/)

> Watching a famous guy much smarter than I struggle for more than 30 minutes to
> not quite solve the problem his way (there was a bug) made quite an
> impression. It brought home to me once again that "point of view is worth 80
> IQ points." I wasn't smarter but I had a much better internal thinking tool to
> amplify my abilities. This incident and others like it made paramount that any
> tool for children should have great thinking patterns and deep beauty
> "built-in."

### Periphery

If your reasoning is hindered by cognitive overload while trying to solve a
problem, and there's no clear first step toward a solution, take a step back and
start working with the Periphery. By cleaning up the periphery, you'll often
find that the core problem becomes clearer and more approachable.

A good example is legacy code: issues in the periphery, such as poor variable
names, bad code formatting, or a disorganized folder structure, may seem
irrelevant to the core issue. However, they still contribute to the cognitive
overload.

Unclear or messy periphery can be a constant attention sink. It leads to
mistakes, confusion, and delays, especially when teams don't take the time to
fix it. Recognizing periphery issues and acting on them is a skill in itself. It
helps to keep your mental state clear and reduces unnecessary mental work.

Some examples of periphery issues:

- **Naming**. Folders, files, documents, tools, and conventions. Poor or
  inconsistent naming alone can create significant noise.

- **Code formatting**. Inconsistent or sloppy formatting adds friction for
  everyone.

- **Structure**. Disorganized codebases or documentation make it hard to find
  and understand things. See also: "Encyclopedic Document".

- **Responsibilities**. Incorrect or unclear class and component
  responsibilities, even far from your immediate task, add to cognitive load.

Another word for Periphery is Background, see also
[Deconcentation of Attention](http://deconcentration-of-attention.com/).

### Rational and Unconscious

Engineers create rational artifacts that may appear simple and mundane. However,
the process behind their creation often involves deep reflection and can stem
from the unconscious mind.

### Engineering as Input/Output: The Role of Prepared Inputs

An engineer can be thought of as an I/O device that transforms inputs into
outputs. The output, a solution or an implementation path, is often clear when
the inputs are well-prepared and mature.

When someone struggles to solve a problem, it is worth examining the quality of
the inputs. Some may be missing, incomplete, inconsistent, or incorrect. Once
enough information is collected and clarified, the solution often emerges
naturally.

Inputs can take many forms: a precise task definition, a clear system
description, a solid understanding of the environment, personal experience and
skills, well-formed mental models, effective diagrams, synergies with existing
components, or advice from a fellow engineer. The healthier and more complete
the inputs, the more straightforward the path to a solution becomes.

### Humans are not designed for Big Numbers

If you have to work with something that involves a big number of entities, like
do something on 10000 files or work with megabytes of data, start with reducing
this quantity to a minimum possible number of entities so that still makes sense
for a prototype of your final work: make it work with 1 file instead of 10000 or
with 20 bytes instead of 20 gigabytes.

### There is no such thing as Many

Many does exist but it is difficult to cognize with a human mind. Many needs an
Umbrella, that turns it into One in the way we think about it. Many can be
homogenous like Array of objects of the same type or heterogeneous, for example
a bunch of instructions in the code or multiple functions in a test class or a
set of User Profile fields of various types: name (string), age (int), settings
(object). Collections are easier because they hide Many from us behind a
well-defined interface: `containsObject`, `getAtIndex`, `enumerateWithIndex`,
which saves us from dealing with Many directly. Heterogeneous Many is harder:
you have to cognize and organize it yourself: group instructions into meaningful
functions, group fields into meaningful containers like structs or database
tables.

One programming construct that fails to constrain Many is tuple: you start doing
things like `let person = ("John", 32)` and `let (name, age) = person` or things
like `person.1` but then you quickly find yourself in a mess when the number
grows to a real Many (quick lesson: don't use tuples, use structs!). If you have
Many, find a way to think and work with it like One.

### 0-1-2-Many I

Most of the people start saying "so many", "infinite" when there is actually 3
or 4, rarely more, things on the table. Variation is 1a, 1b, 2a, 2b which is
still within limit of 3 or 4. This looks like ancient calculator: when 0, 1, 2
and then 'many'. Algebra looks fairly simple: 0 + 1 = 1, 1 + 1 = 2, 2 + 1 =
many, 2 + 2 = many, etc. Consequence: people are quite susceptible to small
numbers. Say something like "this consists of 3 steps" and people will get it.
Don't say "seven". See also **Humans are not designed for Big Numbers**.

### 0-1-2-Many II

Don't start to abstract or DRY from just two things. Wait until you have at
least 3 of them. See also **Duplication is better than poor abstraction**.

### Masking (Shadowing)

Masking, also called shadowing, is dangerous and should be avoided or handled
with great care. It happens when one thing looks or means almost the same as
another thing. Because of this similarity, it is easy to confuse one with the
other. This makes the system harder to understand.

The main problem with masking is that it hides important information. Real
differences become difficult to see. People may make assumptions without
noticing them. As a result, developers can build a wrong understanding of the
system. Masking can lead to small bugs, wrong implementations, bad decisions,
or, in serious cases, larger system or project failures. Very often, such
problems are discovered late because everything looks correct at first sight.

Typical examples include:

- Overlapping or very similar requirements that are implemented over time and
  later cause inconsistent or conflicting behavior.

- Shadowing of variable declarations, where a variable in an inner scope hides a
  variable from an outer scope.

- Using the same variable name in similar or overlapping contexts, which
  increases the risk of confusion.

- Typographically ambiguous symbols that look similar, such as l and 1, or O and
  0 (see MISRA guidelines).

- Code reviews, where real bugs are hidden by more visible but less important
  issues, such as typos or small style problems.

- Masking effects in MC/DC, where tests look complete but do not really separate
  important conditions.

- High complexity, where bugs hide behind many layers or unnecessary details.

In general, masking reduces clarity and increases mental effort. Systems with
masking are harder to understand and more likely to cause human errors.

See also: Overlapping Control.

### Weighting system

I often visualize software-related decision making and trade-offs, both in my
systems engineering work and in discussions with fellow engineers, as a system
of weights placed on a scale. When a decision is hard to make because there are
conflicting arguments or interests, it is like a perfectly balanced scale where
all weights cancel each other out. Each weight represents a particular quality
that we care about. For example, we may value the observability of a system, and
this value will drive many of our decisions, outweighing other aspects that may
be in conflict with it, for example, performance or the desire to avoid
cluttering the code with unnecessary tracing calls.

Sometimes the weights can be distributed too evenly, outweighing each other
without any particular weight (decision) gaining dominance. This leads to the
risk of unresolved trade-offs that drag on for too long. At other times
discussions get heated because the weights of the participants are not fully
synchronized. Reaching agreement in such situations is almost like synchronizing
a combined weighting system that includes the weights of every participant in
the engineering group. Once the weights are recognized, made explicit, and
agreed on, some weights become heavier (that is, more important) and some lose
their weight. When all participants share the same summed-up weighting system,
the scale finally tilts, and that is when the decision is made.

The unfortunate part is that the entire decision-making process is limited by
the knowledge of the participants. Depending on the available information, the
scale may fall toward a decision that later turns out to be right or wrong. So
the game of weights, even when played carefully and with good intentions, does
not guarantee that the resulting decision will lead to the best or most
practical outcome.

It is not easy to quantify the strength of certain qualities because they are
context dependent and can also vary based on the individual experience of the
people involved.

The weighting system of a highly experienced professional can be much more
multidimensional and nuanced compared to that of someone who has just started
their software engineering career.

One important function of onboarding and early code and design reviews, when a
new colleague joins an existing team, is the synchronization of the weighting
systems that the person and the team have. Sometimes the team's weighting system
is stronger and more rational than that of the newcomer, and sometimes it is the
other way around.

## Design

### Functional analysis and decomposition

Before implementing a system in software or hardware, it is essential to
understand what needs to be done, assign tasks and interfaces between teams,
plan the work, and allocate resources. A common approach to achieve this
understanding is Functional Analysis, which enables Functional Decomposition,
also called Functional Partitioning.

Functional analysis focuses on what the system must do, rather than how it is
implemented. At this stage, logical-not physical-aspects of the system are
analyzed. The primary goal is to identify system functions and their
relationships.

An early outcome of this analysis is a preliminary functional block diagram,
which splits the system into logical parts. Once the system's contours are
defined, the next step is to determine meaningful interfaces between these
blocks. Well-defined interfaces ensure modularity and clear interactions when
the system is implemented physically.

The challenge is to partition functions efficiently, avoiding over-engineering
while maintaining flexibility and clarity. If the initial splitting of functions
is inefficient, the functions are regrouped, producing a new version of the
functional decomposition. This process is repeated iteratively until the
following conditions are met:

- All functions are captured, leaving no gaps in functional coverage.
- All functions are partitioned in the most efficient way, given the team's
  knowledge and experience.
- All functions are ready to be transformed into a work breakdown structure
  (WBS) that makes sense from both programmatic and technical perspectives.

When functions are well-separated, mapping them into future work packages
becomes straightforward. For example, Function 1 can become Work Package 1,
Function 2 becomes Work Package 2, and so on. Aligning tasks with functions
allows teams to focus on their work independently while interacting through
clearly defined interfaces. This alignment improves efficiency and minimizes
blocking between teams.

Effective functional partitioning leads to a robust WBS and clear separation of
responsibilities. Conversely, poor or incomplete functional analysis can result
in inefficiencies, unclear responsibilities, and slow progress.

Besides supporting the derivation of the WBS, functional decomposition also
enables other activities that contribute to robust technical work partitioning.
For example, safety, reliability, performance and other analyses can be carried
out early in the project, even before actual technical development begins. A
well-structured functional decomposition can support these analyses efficiently
and provide feedback that may suggest more optimal functional splits, resulting
in a safer, higher-performing, and more efficient system. Early integration of
safety analysis into functional design helps prevent risks and potential
accidents, avoiding issues that could arise if safety considerations were
delayed.

Functional decomposition is recursive. After identifying top-level functional
blocks (e.g., F1, F2), each block can be further decomposed into sub-functions
(e.g., F1.1, F1.2). Complex projects may produce a deep functional tree, with
higher levels managed by the core team and lower levels delegated to suppliers
or subcontractors.

An excellent quote from Systems Engineering Fundamentals captures the essence of
functional decomposition and partitioning:

> **Functional Partitioning** Functional partitioning is the process of grouping
> functions that logically fit with the components likely to be used, and to
> minimize functional interfaces. Partitioning is performed as part of
> functional decomposition. It identifies logical groupings of functions that
> facilitate the use of modular components and open-system designs. Functional
> partitioning is also useful in understanding how existing equipment or
> components (including commercial) will function with or within the system

See
[SYSTEMS ENGINEERING FUNDAMENTALS](https://ocw.mit.edu/courses/16-885j-aircraft-systems-engineering-fall-2005/6128a102c1a9b6dbd30f2fb18c12aa64_sefguide_01_01.pdf).

### Poor Abstraction

> Duplication is better than poor abstraction (Sandi Metz, Rails Club 2014,
> Moscow).

> "...ill-fitting structure is worse than none..." (Eric Evans - Domain-Driven
> Design, p.446)

A good example from https://www.sigbus.info/worse-is-better:

> In lld v2, we decided not to use an intermediate representation. Instead, we
> directly handle platform-dependent native file formats. lld v2 consists of
> virtually three different linkers for Windows, macOS and Unix. They share the
> same design but do not share code. Naturally, we sometimes had to write very
> similar code for each target. This may seem like an amateur-level programming
> mistake, but in reality, it's much easier to write straightforward code for
> each target than writing unified one that covers all the details and corner
> cases of all supported targets simultaneously.

### Cost of Abstraction

Software engineering often involves creating abstractions. A solution to a
problem can include more or fewer abstractions, but each introduced abstraction
comes with a cost. This cost manifests as the cognitive burden placed on those
who need to understand, maintain, and document it - not just in code, but also
in models, documentation, and even organizational structures.

Cognitively, an abstraction can be thought of as a mental gadget that one must
"install" in order to work with it. Imagine an empty room that needs to be
furnished according to a specific use case. If the chosen abstractions fit well
within the team's mental model, the space remains functional - like a
well-furnished room where people can move freely and use it as intended.
However, if abstractions are difficult to grasp or combine in contradictory
ways, the mental space becomes cluttered, leaving little room to maneuver. This
is similar to a room overloaded with furniture, making it difficult to navigate
or even understand its intended purpose.

For example, if a team introduces a new abstraction X, it incurs the following
costs:

- Every developer must understand and adopt X to work effectively within the
  system.
- The system must be structured around X in a way that ensures maintainability
  over time.
- Long-term maintenance will require keeping the code, file structure, and
  models aligned with X, often introducing additional overhead.

Introducing too many incompatible abstractions - or a few abstractions that
consume too much of the decision space - can quickly lead to over-engineering.
Those responsible for maintaining such systems often find themselves
disentangling unnecessary complexity, seeking a new balance that restores
manageability by replacing or introducing more adequate abstractions.

### Habitability

Habitable software is better than perfect software.

[Richard Gabriel - Patterns of Software, Habitability and Piecemeal Growth](https://www.dreamsongs.com/Files/PatternsOfSoftware.pdf).

> Habitability is the characteristic of source code that enables programmers,
> coders, bug-fixers, and people coming to the code later in its life to
> understand its construction and intentions and to change it comfortably and
> confidently. Either there is more to habitability than clarity or the two
> characteristics are different...

> ...Habitability makes a place livable, like home. And this is what we want in
> software - that developers feel at home, can place their hands on any item
> without having to think deeply about where it is. It's something like clarity,
> but clarity is too hard to come by.

### Hard Things

If something is hard to implement or hard to work with, it might indicate that
there is something wrong with it. Not all things are healthy in the end, so one
must recognize what is worth pursuing and what needs to be flagged as unworthy.

This applies not only to product features, but to everything we work with:
software components or architectures designed by us or by others, third-party
libraries, and even project plans or product visions. When an idea, abstraction,
or dependency consistently resists implementation or integration, the difficulty
itself can be a signal that the underlying concept is unclear, overcomplicated,
or mismatched with reality.

### True Name

If you know [True Name](https://en.wikipedia.org/wiki/True_name) of something
you have power over it. Good class name - this is what True Name is in OOP.

> "A well-chosen word can save an enormous amount of thought", (said by Mach
> according to S.R.Cajal, Santiago Ramón y Cajal, "Advice for a young
> investigator")

See also
[Mass and Gravity](http://www.carlopescio.com/2008/12/notes-on-software-design-chapter-2-mass.html).

### One Pattern per Class

A class violates Single Responsibility Principle if it contains implementation
of more than one design pattern. Of course there are exceptions.

### Archetype

Archetype is an umbrella concept for other concepts like: `prototype`,
`proof of concept`, `minimal viable product`. Archetype means something simple
and coherent. If you know the archetype of something you understand the essence
of it. A complex system can be traced back to a one or a number of underlying
archetypes.

Interesting side note: as far as I see it, the tendency is that engineers as
they grow their software bigger, do not care much about the underlying
archetypes. Imagine how easy it would be to learn about the software if it would
contain itself in its earliest forms of being (source code, documentation,
drafts etc). Great example: Rust programming language had to start from
[somewhere](https://github.com/graydon/rust-prehistory).

> "View the problem in its simplest forms ... An excellent method for
> determining the meaning of something is to find out how it comes to be what it
> is." (Santiago Ramón y Cajal, "Advice for a young investigator")

### Prima Materia

Sometimes to make further progress you need to un-implement (break!) particular
pattern/architecture/solution and put it back into
[Prima Materia](https://en.wikipedia.org/wiki/Prima_materia) state and only then
thansform it into a something new. Metaphors similar to Prima Materia are
"primordial soup" and "indifferentiated soup of ideas" (Eric Evans - DDD).

### Mature automation

Mature automation allows itself to be observed, inspected, and overridden. Even
if something is automated and usually works well, there should always be a way
to turn it off or adjust it when needed. Good automation is transparent - you
can see what it is doing, understand how it works, troubleshoot problems, and
make changes if necessary. In some situations, it is important to bypass
automation entirely and take manual control or use an alternative path. Systems
that do not allow this create unnecessary friction and risk. Automation should
support people, not trap them.

### "Magic" is automation that is not adequate

In the beginning, there is no magic, but simply a desire to automate things to
reduce repetition. Magic appears as a result of increasing complexity that makes
current solution to be inadequate for further progress. Magic can also emerge
rather quickly as a result of automating wrong things from the beginning. The
holy grail is automation that is always adequate.

### Poisonous Systems

Badly designed systems tend to poison systems they interact with.

### Bad Design in House

Do not overdesign your own software if you have a big producer of bad or too
opinionated designs nearby. A big producer can be a vendor or a team with
authority who decided to rely on a given design a while ago.

### Unnecessary Flexibility

(from [Writing Solid Code](http://writingsolidcode.com/))

> Flexibility breeds bugs. Another strategy you can use to prevent bugs is to
> strip unnecessary flexibility from your designs... The trouble with flexible
> designs is that the more flexible they are, the harder it is to detect bugs.

> ...Flexible features are troublesome because they can lead to unexpected
> "legal" situations that you didn't think to test for even realize were
> legal...

> ...When you implement features in your own projects, make them easy to use;
> don't make them unnecessary flexible. There is a difference. Don't allow
> unnecessary flexibility.

### Black Box with a Green Play Button

Ideal interface for a system of arbitrary complexity is a black box with a green
play button on it - you take the box, press green button and it just works. The
second ideal interface is when you also have a red button to stop the system.

### Single Source Concept and Its Exceptions

The Single Source (of Truth) concept is one of the first principles beginner
programmers learn and often becomes a rule they follow rigorously. However, like
many principles in life, it has its exceptions. Blindly adhering to the Single
Source rule can sometimes lead to suboptimal results.

A good example of when this principle might fail is the
[Poor Abstraction](#poor-abstraction) scenario. This happens when someone tries
to consolidate similar elements into a single source while ignoring their
significant differences. In such cases, forcing everything into one place can
create an abstraction that is brittle, confusing, or overly complex, ultimately
making the system harder to understand and maintain.

Another example is
[Two Almost Identical Entities](#two-almost-identical-entities). This occurs
when someone tries to merge two seemingly identical entities into one, which
results in an overly complicated "Single Source of Truth" codebase. This
approach often leads to significant branching logic and reduced readability,
making the code harder to work with and more prone to errors.

Understanding when to apply the Single Source principle and when to allow for
exceptions is crucial for achieving balance and maintaining flexibility in
software design. Learning where to follow and where to de-prioritize the Single
Source principle is a good skill that distinguishes a more experienced
programmer from a beginner one.

### Resilience to Change vs Fixed Perfect Solutions

When designing a system, there is a trade-off between making it easier to change
in the future and striving for perfection. In most cases, choosing flexibility
is the better option. If you anticipate changes in context or additional
development work that could affect the system, avoid focusing too much on
perfecting the existing solution, as it may not hold up under new pressures.
Another important consideration is the ability to undo or disable a function
that works perfectly now but could cause unforeseen issues in operation. Often,
a perfectly working solution can create obstacles for other systems or people
involved in operating the system.

### Two Almost Identical Entities

Over the years I have seen at least three big units of a hardly manageable
legacy code where each of them was built on two almost identical entities. There
are two ways of such things to co-exist:

1. One is a subclass of the other.
2. Two almost identical hierarchies are maintained.
3. Two groups of helper functions without a clear separatation of
   responsibilities between them.

It seems that historically in all three cases it started with one entity that
accumulated its features along the way, then came the other which was so similar
to the first that programmer avoided extraction of similar modules that both
entities had and went with subclassing to get the result quickly or with 2
parallel hierarchies.

To these days I still didn't see or create an elegant solution to this problem.
See also "Hard Feature".

### Design for Operations

When designing a system, consider how it will be operated in production. A
system may be operated entirely by humans, partially automated with human
oversight, or fully automated. In all cases, the system must be accessible to
its operators in terms of understanding, control, observability,
maintainability, and other operational aspects.

The challenge in design is that developers often have a limited view of the
system, especially of the final and actual environment in which it will operate.
It may require special training and a continuous, conscious 'systems thinking'
effort to put oneself in the operators' shoes and properly identify the
properties the system must have to be easily operable and maintainable.

### Control

One of the key concerns is Control: where control should or should not be, what
should have control (be active) and what should not have (passive).

#### Observable Control

Software should be designed in such a way that there always should be a
dedicated place where it is obvious how the control and work flow through the
software. This should be effective on all levels of abstraction and for each
level of abstraction, such dedicated software should be free of the lower-level
implementation details that discourage easy understanding of context.

If something creates a low-level implementation noise on a given level, it might
be a good sign that one or more underlying lower layers exist where that
lower-level implementation can be represented as a high-level workflow logic
(sequence of steps or algorithm).

#### Humans should dominate machines

The lower-level modules should not have control over higher-level modules. It is
not only about not having higher-level module imported in lower-level modules
and making everything to work through protocols/interfaces but more about what
is the flow of control: "what controls what". Two shortcuts: **humans should
dominate machines**, **business logic should dominate the system's
implementation details**.

#### Overlapping control

Overlapping things is a challenge for a human mind and therefore is bad for the
whole software lifecycle: design, development, testing and maintenance. This
might be two or more classes that do the same thing. This might be two or more
people whose responsibilities overlap. Nancy Leveson says Overlapping Control is
one of the greatest sources of safety problems: two controllers whose areas of
responsibilities overlap (see "Engineering a Safer World"). See also "Two almost
identical entities" and "Shadowing/Masking".

#### Broken control loops

The top-level controllers should always have a control over the bottom-level
elements. If the controllers include both humans and automation, the humans
should always be able to intervene and take over the control provided by the
automation.

This heuristic can be turned into explicit design constraint.

### Feedback

#### Broken feedback loops

Missing, insufficient or incorrect feedback is a great source of troubles for
any system.

"All feedback loops must be closed" - this heuristic can be turned into explicit
design constraint.

### Separation / partitioning

- Separate stable from unstable
- Separate permanent from temporary
- Separate synchronous from asynchronous
- Separate similar from different
- Separate symmetrical from asymmetrical
- Balance and symmetry: if one partition has way more items than the other ones,
  this may indicate that the partitioning has not been complete.
- Separate construction from operation (one example: Factory vs Command)
- Separate content from presentation (applies to UI-heavy code, great example:
  HTML/CSS)
- Separate easy from complex: isolate easy, isolate complex, repeat many times
- Separate stateless from stateful
- Separate data from behavior and behavior from data unless you do have a good
  OOP class/object with good data/behavior balance.
- Separate general-purpose from application-specific
- Separate application-level code from system-level code
- Separate methods that read from methods that write
- Separate decision from condition
- Separate/abstract interface from implementation
- Separate One from Many, separate Many from Many.

Example 1: "Monolithic test case files"

In the following example the `_feature1_` or `_feature2_` parts and numbers in
the test method names assist a lot in logical grouping of the tested
functionality.

```c
# Many group #1
test_feature1_1() {}
test_feature1_2() {}
test_feature1_3() {}
# Many group #2
test_feature2_1() {}
test_feature2_2() {}
test_feature2_3() {}
```

Example 2: the inner block has a multiline routine which could actually be
another function that works on one. At the same time this inner block on many.
Unless we create that another function we have a conflict between many of the
enumeration and many of the instructions inside a block.

```cpp
EnumerateInstructions(*function, [&](Instruction &instr, int bbIndex, int iIndex)
{
  ... lots of lines working on `instr` ...
});
```

### Trade-off of Encapsulation

Strong, "tight", encapsulation is good but don't forget about the users:
Operations people. Good example is debugging facilities - if you close
everything then you leave the ops people, who might be you, without any tools to
understand or tweak your system. Richard Cook explains this very well: See
[Velocity 2012: Richard Cook, "How Complex Systems Fail"](https://www.youtube.com/watch?v=2S0k12uZR14).

### Grouping

- Group together things that change at the same time. If possible create
  container data structures so that a change involves a change of **one**. If
  possible, group all the changes that happen at the same time together.

- Group things that are used together.

### Observability vs Correctness

Incorrect but observable code can be more valuable long-term than correct but
unobservable code. Observable code is easier to inspect, test, and improve, even
if it contains mistakes. In contrast, correct but hidden code can become
difficult to maintain and debug over time, creating technical debt. Visibility
allows for quicker fixes and ongoing improvement, making it more sustainable in
the long run.

### Don't Use RAII on a Business Logic Level

RAII is good for resource management, such as handling memory, file handles, or
network connections, where resources need predictable acquisition and release.
However, applying RAII to business logic can lead to significant problems:

- Reduced flexibility: RAII assumes that actions are tied directly to scope, but
  business workflows may need to defer, combine, or otherwise manage actions
  independently of object lifetimes.

- Lack of transaction control: Business operations often involve external
  systems, validation, or rollback mechanisms that require precise control. RAII
  hides these processes behind object lifecycle management, making it harder to
  handle errors or maintain consistency.

- Unintended side effects: Business logic often involves workflows with complex
  rules and dependencies. Tying actions like adding or removing data to the
  lifecycle of objects can cause unexpected behaviors if those objects are
  destroyed prematurely or unintentionally.

- Debugging challenges: When business actions are implicitly triggered by object
  lifetimes, it becomes harder to trace when and why specific operations occur.
  This lack of clarity can lead to subtle bugs that are difficult to identify
  and fix.

Instead of using RAII, manage business logic explicitly through well-defined
methods or services. This approach keeps the logic transparent, easier to
understand, and more adaptable to changing requirements.

### Rich Collection of Models and Diagrams

Since each model or diagram represents only a fragment of reality, no single
view is sufficient for engineering work. To address different tasks effectively,
an engineer needs access to a diverse set of models and diagrams. Each
representation emphasizes some aspects while concealing others, so a rich
collection ensures that the essential dimensions of reality can be examined from
multiple perspectives.

An engineer with a diverse set of modeling tools can communicate design ideas
and reasoning far more effectively than someone who relies on no visuals or only
a single type of diagram. Multiple representations improve clarity and ensure
that all relevant aspects of the system are adequately considered.

The Unified Modeling Language (UML) offers a good illustration. Its suite of
diagrams is designed to capture both structural and behavioral aspects of a
system. Class and component diagrams clarify static structures and their
relationships, while sequence, activity, or state diagrams describe dynamic
behavior over time.

### The Limits and Choices of Models and Diagrams

Models and diagrams represent selected aspects of reality. By definition, each
one captures only part of what it describes. The choice of a particular model or
diagram shapes which information is highlighted and which is hidden or
downplayed.

This has practical consequences. If the task at hand does not align with the
purpose of the chosen model, the model may become distracting rather than
useful. A representation that clarifies one dimension of a system may obscure
other aspects that are crucial for solving the problem.

For example, a static diagram showing functional blocks and their interfaces can
clarify structural relationships, but it gives little insight into how those
functions interact over time. Conversely, a time-based activity diagram
illustrates temporal interactions well, yet it can obscure the functional
grouping of elements.

Reliability and safety analysis provide another illustration. A static
structural diagram can show how many elements exist and how they are grouped
within a system or repository. Such a view offers an inventory of what can, in
principle, be analyzed. However, it says little about control dependencies, how
failures propagate, how redundancies work, or how safety properties can be
assured.

Recognizing these limitations is essential. An architect, safety analyst, or
engineer who understands the inherent constraints of models is better equipped
to request or create additional representations when needed. Without the right
models, or in the presence of misleading ones-analysis, design, and
decision-making can suffer.

### Pseudocode as a Modeling Tool

Sometimes a fragment of pseudocode can capture the essential aspects of a
process more effectively than an activity diagram. Where diagrams may become
cluttered with blocks and arrows, pseudocode can provide a direct and precise
description of the logic, making it easier to understand and communicate.

## Coding, code reviews, and maintenance programming

### Code that Works

Working code with a good-enough architecture is better than buggy code with a
perfect but overly complex architecture.

### Code Is Not Your Partner

Sometimes, you don't have to be nice to code.

- It might be written for a different platform.
- It could be outdated or rely on ancient build tools.
- Some parts may be unnecessary for your needs.
- It may contain mistakes.

In such cases, it is perfectly fine to delete, modify, or hack the code - to
make it compile, test it, or simply understand how it works.

### Two Strategies for Replacing a Feature

When replacing Feature A with Feature B, there are two broad approaches.

1\. Remove A, Then Implement B

This strategy is best when:

- Feature A is simple.
- Feature B can be developed quickly.
- Switching to B is straightforward.

In such cases, removing A first and then building B works well, as the
transition is fast and manageable.

2\. Develop B in Parallel, Switch from A to B, Remove A

This approach is necessary when the transition is complex or time-consuming.
Instead of removing A immediately, B is developed alongside it while the
existing system remains operational. The switch to B happens only when it is
fully developed and tested. A remains available as a fallback until B is proven
reliable, after which A can be removed.

This method is particularly useful when:

- Feature B requires significant development time.
- Switching from A to B is complex and requires a dedicated transition
  mechanism.

For already deployed systems where downtime is unacceptable, the second approach
is often the only viable way to ensure a smooth migration.

### Smallest Scope

- Restrict the scope of data to the smallest possible. (The Power of 10: Rules
  for Developing Safety-Critical Code by NASA)

### Code Style as a Blocker

Sometimes code style can be a blocker. Poorly formatted code can make
understanding of it extremely difficult. Do everything to reduce your cognitive
load. Real-world example:

```swift
let expectedRemainingLoops = Int(ceil( (expectedRemainingElements - Double(currentRemainingElementsForLoop)) / Double(PPENumberOfTasksInCurrentLoop) ))
```

reads much better if

```swift
let expectedRemainingLoops =
  Int(
    ceil(
      (expectedRemainingElements - Double(currentRemainingElementsForLoop)) /
      Double(PPENumberOfTasksInCurrentLoop)
    )
  )
```

### Avoid Plural Names For Classes

Classes should represent a single entity or concept. Naming a class in the
plural form (e.g., `Users`) can confuse its responsibility, making it seem like
it manages multiple instances. Instead, use singular names (e.g., `User`) and
handle collections separately, such as in a `UserList` or `UserRepository`. This
ensures clear, focused class responsibilities.

### Fast Programming and Slow Programming

This can be viewed as prototype vs. maintenance programming. Fast Programming is
crucial for rapid progress and is often encouraged by the business. However, it
rarely allows time to learn from mistakes due to the tunnel vision and "straight
ahead" thinking that often accompany it. Slow Programming, on the other hand,
has the virtue of reflection and deeper analysis, but it tends to be too slow to
launch a business from scratch. Business leaders typically start to appreciate
Slow Programming only when they hit the wall of complexity, realizing the need
for proper design.

### Stable Components

Stable Components is a resort of a Maintenance Programmer. One way for a
developer to survive in a large legacy project is to create stable components or
extract them out of existing mess of code. Stable component most likely means a
testable component: it can be a parsing module or API layer or string
manipulation helpers. Having such islands of stability helps a lot to overcome
the difficulties of a maintenance programming. See also Periphery and Prima
Materia Heuristics.

### Boring Code

(from [Writing Solid Code](http://writingsolidcode.com/))

> If your code feels tricky, that's your gut telling you that something isn't
> right. Listen to your gut. If you find yourself thinking of a piece of code as
> a near trick, you're really saying to yourself that an algorithm produces
> correct results even though it is not apparent that it should. The bugs won't
> be apparent to you either.

> Be truly clever; write boring code. You'll have fewer bugs, and the
> maintenance programmers will love you for it.

### Boring Code 2

Complex software is not to be developed and used by average programmers. This
happens anyway because of production pressures. People say: your mileage may
vary.

### Lack of Knowledge

Bad code stems from a lack of knowledge, not malice, even though both bad code
and malice share unawareness as their root cause. Sometimes, it helps to put on
a "lack-of-knowledge hat" to better understand the intentions behind the code
you're reading.

### Lack of Knowledge II

An interesting feature of inexperience is that it imposes limits on a software
system's ability to scale. Software written with unawareness at its core will
eventually become rigid and nightmarish, to the point where team members start
avoiding the "dark forest" of its codebase. The natural consequence is that such
software reaches an upper bound of complexity. Paradoxically, this means that
someone tasked with re-engineering it will often find its complexity manageable
in the end.

### Goodwill vs Pain

Much of what we programmers learn over the years comes from pain, not from
goodwill.

## Version control, Git, code reviews

### Simplifying Complex Feature Branches

When working on a non-trivial feature branch, consider breaking it down into its
core functionality while separating any trivial or unrelated changes that can be
integrated independently.

A complex branch can often become more manageable, or even medium in scope, when
distilled into its essential parts and split into smaller, separate changes. In
some cases, breaking it down properly can eliminate the complexity entirely,
leaving only straightforward, incremental updates.

### The Moving and Changing Anti-pattern

A great anti-pattern that complicates code reviews is creating a changeset that
involves both moving and changing things at the same time. This obscures the
diffs in the version control system, making it harder to track changes. The
solution: isolate moving and changing into separate commits or separate PRs.

### Git commit names: Context: Title

My experience of reading commits shows that I read commit titles better when
they clearly indicate a context. A commit context can be the name of a topic of
work, a software component name, or a software component folder. If I see a
commit in the form context: title, I immediately recognize that it is about
something within the scope of that context.

The Conventional Commits specification implements this idea nicely because the
context is placed inside parentheses, for example: feat(parser): support
multiline attributes or fix(ui): prevent crash on empty input. Even without
reading the commit body, the reader can quickly classify the change and decide
whether it is relevant.

In practice, the exact syntax matters less than the consistency of applying the
idea. A short, stable context followed by a concise title significantly reduces
cognitive load when scanning git log, reviewing pull requests, or searching
through history.

Sometimes the context can be omitted if the commit message itself tells enough
of the story, especially when a project is just starting or is very small. Most
of the time, however, I find that using a context is very useful.

## Biases

### If It Works, Then It Works Bias

One of the common cognitive biases in engineering is the assumption that if
something works, it must be good enough. This belief often surfaces during
reviews of code, design, or systems that have passed tests or are known to
function under specific conditions. It takes conscious effort to question
something that already appears successful.

But just because something works under one set of constraints does not mean it
will hold up under others. Often, "it works" simply means "it works here and
now".

To counter this bias, reviewers should look beyond surface-level functionality
and ask:

- It works with a file of size X. What about 10X or 100X?
- It works under normal conditions. What about a slow network or high CPU load?
- It works on Linux. Will it behave the same on embedded hardware?

This bias also affects how we treat existing systems. A solution that "has
always worked" may be treated as correct by default, leading to investigations
based on flawed assumptions and missed problems that emerge under different
circumstances.

There's no silver bullet for overcoming this bias. The key is maintaining
deliberate skepticism and making a habit of viewing solutions from multiple
angles.

### Focusing only on what's most visible bias

The tendency to concentrate a review or investigation on the most obvious,
observable, or symptomatic parts of a system, rather than systematically
considering all potential contributing factors. This can lead to overlooking the
true root cause, especially if it's hidden in a less familiar or less accessible
area. Before jumping on a specific part of the problem or solution, first step
back and consider the bigger picture - which blocks in general might be
involved. As per the common saying: "Don't look only where there is light". In
practice, this means listing all possible contributors to a problem in the form
of a block diagram or any other simple sketch that collects both the symptoms
and relevant system parts. It can also help to annotate each block with relevant
properties - for example, in a performance investigation, adding performance
characteristics per block can highlight which parts are likely causes, not just
the ones that appear most problematic.

### The Fix Bias

When reviewing a pull request titled "Fixes XYZ", there is a natural tendency to
trust the new change more than the existing code. This bias arises from the
assumption that the previous implementation was flawed simply because it is
being replaced. As a result, one might overlook the consequences of the fix or
fail to rigorously verify the correctness of the new change.

To mitigate this bias, it's important to evaluate both the old and new
implementations with equal scrutiny. Consider questions such as:

- Is the problem being solved accurately identified?
- Does the new change address the issue without introducing new problems?
- Are the trade-offs of this fix justified compared to the original
  implementation?

By being aware of this bias, reviewers can ensure a more balanced and thorough
review process.

### Resolving Merge Conflict Bias

Software engineers frequently resolve merge conflicts, and while this task is
often trivial, it presents opportunities for introducing subtle bugs. One
contributing factor is the cognitive bias that favors accepting newly introduced
changes over preserving existing behavior.

The conflict markers (`<<< >>>`) used by Git can obscure important details of
the original code, making it easy to unintentionally discard necessary logic.

A practical approach to mitigating this risk is to slow down and carefully
evaluate both conflicting versions. Consider not just the new change, but also
what might be lost if an existing line or code chunk is removed. Reviewing the
code in context and testing after resolving conflicts can help prevent
unintended regressions.

## Reliability

### Errors are not ok

Never ignore errors. Presence of errors indicates that you don't understand your
system well enough and therefore don't have a full control over it.

An error can be major or minor but it anyway contributes negatively to the
design and operation of your system and also to your understanding of it (see
[Periphery](#periphery)).

Errors typically ignored by developers include:

- Configuration errors
- Compiler warnings
- Build system errors
- Errors produced by the test suites (flaky tests)

### Errors must be understood and described

Google for `Malfunction 54` for a good example.

### Underlying errors shall not be hidden

If a higher-level error wraps some other underlying error, the information about
the underdying error shall not be lost. Instead, it should be fully available to
the higher-level error for error handling, logging, tracing, etc.

### Critical errors vs non-critical errors

Make a clear distinction between critical and non-critical errors on all levels:
source code, software design, error reporting, documentation.

### Assertions are better than no error handling

When there is no error handling, presence of asserts gives at least some basic
guarantee that software does not do what it is not supposed to.

### Assertions are shortcuts for a proper error handling

Every assert becomes a proper error handling eventually.

### Crash Early

If you know how to not program defensively in a particular situation go ahead!
Otherwise make your code to Crash Early to catch bugs as early as possible: use
sensible assertions and stress edge-cases with tests. See
[Some notes C in 2016: Code offensively](http://blog.erratasec.com/2016/01/some-notes-c-in-2016.html#.VtGEKBg7T5c)
and
[Spotify engineering culture (part 2): "We aim to mistakes faster than anyone else"](https://labs.spotify.com/2014/09/20/spotify-engineering-culture-part-2/).

## Testing

### Write Tests, Even Bad Ones

If you do not write tests, you will never learn how to write them. It's better
to write bad tests than to write none at all.

### TDD as a Toolbox

Ability to do TDD is not a binary "can or cannot", it is about having 1001
things in your toolbox: techniques, patterns, tricks and hacks - when you have
enough of them you can test almost everything.

### Legacy Code is Code Without Tests

As Michael Feathers puts it in Working Effectively with Legacy Code, "Legacy
code is code without tests."

### Testing as a Way to Manage Complexity

In addition to ensuring quality, testing is essential for simulations that help
manage complexity. If I can test and simulate every aspect of my program, I can
effectively manage its complexity. However, if there are blind spots - areas
that are difficult or impossible to test - I lose control over those areas and
must rely on real users to test in the wild.

### Test It to Engineer It

"If you can't measure it, then it can't be called engineering" (Ivar Jacobson,
Object-Oriented Software Engineering: A Use Case Driven Approach). We can
interpret "measure" as "test", with testing serving as both a form of
measurement and a core part of engineering.

### Improve Testability

Ideally, we should be able to test everything: if something is hard to test,
then we are simply not there yet with the quality of our code or with the
corresponding toolset and testing infrastructure. But we will manage to find or
improve them and get there.

### Getting the first test to work

If you don't know, or are not sure, how to test something properly, try the
ugliest version first: stub everything in an ugly way, stub the network in an
ugly way, assert what you want to assert, and only then iterate on refactoring
both the test and the SUT (system under test).

### What to Test

When writing a test and there are no clear rules or formal requirements for what
to prioritize, start simple: first test the most common successful "green"
case(s), representing nominal functionality, then add a test for the most
obvious "red" case-error handling in an off-nominal scenario when things go
wrong.

Depending on the problem type and available time, having just one green and one
red case can already provide reasonable initial coverage-often enough for a
feature branch to be safely integrated into the main branch.

For projects with stricter requirements, all possible cases should be covered
immediately. Even then, starting with the first green/red pair can serve as an
easy mental entry point into the testing process.

## Distribution

### Provide Basic Test Sequences with Your Product

If you are a provider of software or hardware, consider going beyond the
standard "interface control document" (ICD) by including basic test sequences -
a "Hello World"-type program that allows users to quickly get started with your
product. Such examples help users bring the system online and get up to speed
without unnecessary guesswork.

The lack of clear "Hello World" or how-to documentation is especially prevalent
in the embedded software industry, where companies often rely solely on ICDs or
technical reference manuals. This forces end-user software engineers to engage
in guesswork and reverse-engineer the documentation to figure out how to bring
up a device. While the industry is gradually improving in this regard, there is
still a long way to go. By providing a clear and functional "Hello World"
example with every product, you empower your users and make adoption of your
product much smoother.

### Provide Drivers Alongside Your Hardware

If you are a hardware provider, consider supplying software drivers with your
device rather than just a technical reference manual for end-users to decipher
and implement. As the developer of the device, you understand its functionality
better than anyone else. By providing ready-to-use drivers, you save your users
the time and effort of implementing the device's features themselves.

With some effort on your part, you can significantly improve the adoption of
your product by making it easier to integrate and use. A smooth setup process
not only enhances user satisfaction but also reduces the barriers to bringing
your hardware to market.

### Provide Simulators Alongside Your Hardware

If you supply hardware, consider providing a software simulator that mimics your
device. This greatly simplifies integration into users' SIL/PIL/HIL setups,
especially if the target users have access to only a limited number of your
devices (such as when the device is very expensive).

For language choice, default to Python, as it is widely used for embedded
development tools. If performance is critical, a C/C++/Rust simulator is also a
great option, as these languages integrate well with embedded environments.

## Documentation

### The Illusion of Easy Documentation

Good documentation is dry and boring. This can create an illusion that writing
good documentation is easy when in fact it is not.

### Software Design Document

No matter the industry, team size, or type of project, every software team
should maintain a document that describes the design and architecture of the
developed system. This document may vary in size - from a few pages to a large,
detailed file - but its purpose is the same: to give any reader a high-level
understanding of how the software is structured and how its key parts work
together.

A good approach is to organize it by topic or component, for example, one page
per software component. Each section should clearly map to something real in the
software, and vice versa. This helps ensure that every major concept or building
block is documented, discoverable, and easy to reason about.

This kind of document might be called a Design Document, Architecture Document,
Design File, or similar, depending on the team or industry. Whatever the name,
its role is the same: to serve as the central, navigable entry point into the
software's structure and design.

### Less prose, more structure

Technical documentation is supposed to focus engineer's attention on achieving a
given goal such as to build a specific system. It is easier to focus one's
attention on things that have structure embedded in them compared to things that
are hidden in several paragraphs of prose. Prose has no structure and that is
why a reader has to do an extra exercise of creating an order out of what they
are reading. If the documentation already has an order in it, the reader can
spend less time for a mental reconstruction of the content and focus on the
technical facts more easily.

Some of the important tools that communicate order in technical documentation:

- Document structure and table of contents
- Diagrams
- Tables.

### Too Much Structure Overload

Excessively deep nesting in documents or folder structures can hinder the
understanding of the overall project or system structure, especially if the
principles used for organizing the sections lack consistency. Ideally, a good
structure should be intuitive, or at the very least, the organizational
principle should be easy to understand and mentally map, facilitating easier
navigation of the content.

### Encyclopedic Document

An encyclopedic document is created over time as a collection of inputs from
various ad hoc events, eventually becoming a generic repository of everything.
These documents often have complex, nested structures and lack a single
consistent narrative. Reading them feels more like going through a dictionary
from A to Z rather than following a coherent story. This can make it difficult
for readers to stay engaged, which might explain why many people shy away from
reading standards altogether.

Standards or guidelines are often structured in this encyclopedic way, as they
aim to encompass all aspects of product development or organizational processes.
Similarly, requirements specifications can easily take on an encyclopedic form,
making them hard to navigate and comprehend.

When creating such documents, it's important to establish a guiding principle
that helps readers mentally map and navigate the content. Ideally, the document
should include a unifying narrative or story that makes it easier to follow,
even if the underlying information is complex or diverse. A clear structure and
logical flow can transform an overwhelming collection of information into a
useful and accessible resource.

## Meetings

### Sound Check

It's great when everyone joins a meeting on time, but an often-overlooked
practice is doing a quick sound and video check to ensure everything is working
smoothly. A good rule of thumb is to join:

- 5 minutes early for routine meetings.
- 15-30+ minutes early for important meetings, to handle any technical issues in
  advance.

### Meeting Agenda

A well-prepared meeting runs smoothly when attendees know what to expect.

- A strong meeting has a predefined agenda that allows participants to follow a
  clear execution plan.
- Is the agenda known in advance?
- Can you or your team define it?
- Are there questions or answers that can be prepared beforehand?

### Meeting Notes

Meetings often lack structure, and when no notes are taken, valuable discussions
can be lost. A better approach is for someone to take ownership of note-taking
in real-time, ideally on a shared screen so everyone can see what is being
recorded.

- If your team owns the agenda, align meeting notes with the planned topics.
- Structure notes so key points and next steps are clear.

### Capturing Meeting Results

A meeting without tangible outcomes is just an expensive conversation. At a
minimum, meetings should result in:

- Action points: tasks, follow-ups, next meetings.
- Decisions made.
- Recognized trade-offs.

Whenever possible, capturing processes or architectures in a diagram is better
than a simple bullet point. Even if no formal notes are recorded, every
participant leaves with takeaways and mental models - but written records
significantly increase the meeting's effectiveness.

Anti-pattern: Running meetings without documenting useful outcomes, leading to
wasted time and repeated discussions.

### Briefing In

Before the actual meeting, getting alignment among participants is key, whether
for internal team discussions or external events like conferences and large
review meetings. When a team participates in an external meeting, it is crucial
that everyone is on the same page and presents a unified front, avoiding any
visible disagreement or misalignment.

Good questions to determine if a pre-meeting briefing is needed:

- How many attendees already know what will be presented?
- Does the content introduce significant innovation that requires prior context?
  Could too much new information create confusion within the presenting team?

Common pitfalls:

- Discussing internal team matters in the presence of external participants.
- Asking too many unrelated questions that derail the focus of the meeting,
  particularly when it disrupts team cohesion and diverts attention from the
  main agenda. This is especially problematic when an individual undermines the
  shared position of the team by introducing misalignment.

### Briefing out

When a meeting involves an external party, it is sometimes useful to meet again
with a smaller group in a so-called debrief meeting to discuss the results and
action points. During such a meeting, the collected information, impressions,
the team's performance during the meeting, and the further strategy can be
discussed to prepare for the next round of exchanges with the external party,
such as a customer, a supplier, or a project partner.

Debriefs can also be useful for onboarding new people into the project work, as
well as for keeping the existing team aligned on the ongoing engineering
activities and the latest project status.

### Sharing Screen & Presenting Material

- Share only the relevant content - close unrelated applications, especially
  internal company chats, before presenting to an external audience.
- If you need to access other files or perform actions outside the presentation,
  unshare your screen first, complete the task, then reshare only the necessary
  content.
- If your team is presenting to an external party, align on the materials
  beforehand to ensure consistency in messaging.

## Systems

### Good enough is often best

"Good enough for each part is often best for the whole system." ("The Art of
Systems Thinking")

In "Engineering a Safer World", Nancy Leveson discusses how, in air traffic
control, individual flight paths may not be optimized for each aircraft to
ensure overall traffic harmony. This approach is necessary because optimizing
each flight path individually could lead to conflicts and inefficiencies.
Instead, air traffic control systems manage traffic by coordinating flight paths
to maintain safe separation between aircraft, ensuring the overall safety and
efficiency of the airspace.

### Designing Systems for Effective Work

- "Rather than trying to find extraordinary people to do a job, design the job
  so that ordinary people can do it well." ("The Art of Systems Thinking")

> ...No one comes to work to do a bad job, but the structure of the system may
> make good work impossible. If management falls into the blame trap, they may
> fire the offending individual and hire someone else - who may do no better.
> Rather than trying to find extraordinarypeople to do a job, design the job so
> that ordinary people can do it well. It is the structure of the system that
> creates the results. For better results, change the structure of the system.

### The Risk of Default Outcomes

Unresolved trade-offs, especially those that persist over long periods, can be
risky. Decisions left undecided, such as whether to build or buy critical
hardware, will not remain open forever. Instead, they tend to resolve themselves
by default, often in bad ways, whether due to inertia, external pressures, or
short-term needs. Like a coin that always falls on a side, an undecided
trade-off will eventually land on an outcome which might not align with
strategic goals.

To mitigate this risk, individuals, managers, teams, and organizations should
proactively track and resolve open decisions, ensuring that critical choices are
made deliberately rather than by default. Tools such as an Open Questions Log or
a Risk Registry can support the structured resolution of such trade-offs.

## People and Organizations

### Everyone is busy

Everyone is busy, including you. The development of software products often
takes place in rushed environments, where everyone is focused on achieving
specific goals without having time to do things properly or fully explore all
the options for what is being built.

How about QA? A company may have a dedicated QA department, or even Safety &
Reliability teams in addition. They are most likely also busy, focusing on the
most critical tasks to the point that they probably don't have enough time to
interact with development teams, understand the real requirements, or provide
100% coverage and a complete assessment of the project scope.

Is it a problem that everyone is busy? Given its ubiquity, it doesn't seem so.
Some people even seem to thrive on being busy all the time. Organizations appear
to care little about "busyness" itself. What really matters is whether the busy
person or department can deliver results according to the schedule or whether
something left uncovered by the busy teams could create serious problems for the
business.

One unfortunate observation is that it usually takes significant time before the
uncovered issues are revealed and addressed from the top down. During this
incubation period, enough money is often lost, a number of unhappy customers
accumulate, and other losses may occur, depending on the type of project.

Or, busy people themselves get tired... and create new methods and tools.
Sometimes, a new tool can eliminate much of the effort required to achieve a
goal, or it simply allows a busy person to focus on "what is most important"
rather than covering everything.

### Solving Problems with Cash

Every engineering problem can be solved with an infinite amount of cash.

### The Paradox of Rushing in Software/Systems Engineering

Attempting to accelerate development often leads to greater delays. In highly
complex systems, skipping thorough validation, testing, or review processes can
result in unforeseen issues, requiring extensive rework and ultimately
prolonging the timeline beyond what a steady, methodical approach would have
taken.

There is one [parable](https://howtopracticezen.org/Advanced%20Zen/) that sounds
like this:

> Zen teachers often tell the story of a young monk who asked a Zen master:
>
> "How long will it take me to attain enlightenment?" The master thought for a
> few moments and replied: "About ten years." The young monk was upset and said:
> "But you are assuming I am like the other monks, and I am not. I will practice
> with great determination." "In that case", replied the Master, "twenty years."

and a [similar one](https://martialarts.stackexchange.com/a/7133/7133):

> ... "But if I work hard, how many years will it take to become a master?"
> persisted the youth.
>
> "Oh, maybe thirty years", said Banzo.
>
> "Why is that?" asked Matajuro. "First you say ten and now thirty years. I will
> undergo any hardship to master this art in the shortest time!"
>
> "Well", said Banzo, "in that case you will have to remain with me for seventy
> years. A man in such a hurry as you are to get results seldom learns quickly."

### Four seasons

It is an amusing analogy: like a year starts with a spring and ends with a
winter, a similar lifecycle can be observed in a growth of organizations.

Spring is a young company, a handful of people. Not much structure, no strict
policies, a startup atmosphere. Not yet a fixed income, but probably investments
or lack of them. More full-stack people with broad expertise. Spring is like a
village. Colleagues are fellow villagers.

A Summer is a Spring that made it, a company that is flourishing. Exponential
growth, more people are hired, extremely steep curve of everything: the
development of the company structure, more departments, more specialization. The
philosophy of the company is no longer about "finding its way" but rather
accelerating on what made a transition from Spring to Summer possible.

Autumn is already a company with legacy. The source of income is known and
stabilized. The responsibilities are defined. Less or no people are busy with
defining a product anymore but more people are busy with the optimization:
improving product, doing sales and increasing revenues.

Winter is a dangerous phase. The company has been making profit and doing its
best by exhausting what was known to work well. At this point, the structure of
the company is the most fixed and therefore the least resilient. The company may
cease to exist because there are younger and more adequate competitors or it can
find a way to renew itself and make it into a new year.

Another interesting observation is that a transition from season to season
almost never goes smoothly - in order to accomodate for change, the company has
to adapt and this very often happens with a good deal of destruction and
restructuring (see Prima Materia heuristic). Dropping what does not work and
keeping or creating what does might be crucial for such a transition. Not all of
the Spring companies make it into Summer. Not all of the companies end up being
Winter. Not all of the companies can survive their deep Winter.

One particular management mistake that can be made is trying to apply the best
practices of a season A to a season B if the season B is too early or already
too late for such an application. Example: imposing a strict top-down style of
management on a company of 5-10 people working in a flat hierarchy and making
them to adhere to the reporting lines might be extremely inadequate as well as
expecting a fully flat hierarchy to work in an Autumn-like business.

Not only we can match seasons and companies, we can also match seasons and
personalities:

- Autumn is too boring for spring people who value creativity and individual
  contribution over hierarchies and defined processes.
- For Autumn people, the Spring is too chaotic and unstructured. Working for a
  Spring company is inherently unsafe: the younger the company, the less
  guarantees it can provide to its employees.
- It may not be optimal for a company to have too many people who represent an
  incompatible season. It can be damaging for a person to get stuck working at a
  company that does not match their season type. In such cases, a person who
  found a matching season can be compared to a fish that found its water.

See also Kent Beck's
[The Product Development Triathlon](https://medium.com/@kentbeck_7670/the-product-development-triathlon-6464e2763c46).
His 3 phases: Explore-Expand-Extract can be loosely mapped to the
Spring-Summer-Autumn seasons.

## Standards

### Idealized standards vs. practical implementation

Standards provide an idealized or encyclopedic view of how systems should
function and how products should be developed. Frequently, a standard represents
the combined inputs of multiple companies, making it more extensive than what
any single company might realistically implement. For most companies,
implementing a standard is a "best effort" exercise.

Some standards are practical only for larger companies and can be
counterproductive or harmful for smaller organizations attempting to implement
them. Recognizing this, some standards explicitly account for a company's
maturity level and offer recommendations on which parts to implement at
different stages of development.

### The challenge of standards implementation

Implementing standards and managing their results within an organization can be
difficult and complex. However, without any standards, everything becomes 10 to
100 times harder and more chaotic.

### Standards and best practices

Standards seek out best practices, collect them, and generalize them.

### Standards favor good practice

Standards favor good practices. If a company has adopted a practice that is not
yet conventional but makes sense and adds value, it is unlikely that this
practice would be rejected or deemed inappropriate by any standard.

### Wrong is worse than early or incomplete

Sometimes it is worse to be wrong than to be early or lack information. The
context: passing the project review milestones required by standards.

### Standards vs Hardcoded Implementations

Standards try to generalize a particular best practice or design approach, but
sometimes this generalization results in a very prescriptive, hardcoded
implementation. When this happens, a standard becomes almost the opposite of
what one would expect from a broad standard - it turns into a tool that enforces
rigid, hardcoded solutions.

Sometimes it can be useful to break away from a given standard to avoid being
confined by its prescribed boundaries. It can take courage to stand up to a
standard and do things one's own way.

Standards may have good intentions but lack the necessary tooling to implement
them properly. In such cases, a tool that does not implement a particular
standard but simply solves a practical problem can be more powerful than the
entire standard itself.

Another interesting case arises when standards compete to be adopted by a
company. If one of the competing standards is simpler, defines a more
straightforward schema and concepts, and is well supported by existing tools, it
may prevail over the other, more sophisticated standard that would require
implementing all its concepts in-house. Sometimes a company may adopt a standard
unintentionally, simply because there is an existing tool that works. In such
cases, the standard operates in the background, and the team can keep using the
tool without even realizing that there is a formal standard or set of
conventions is behind it.

## Requirements

### One-stop shopping

> "One-stop shopping" is a useful requirements writing priciple. Simply, people
> reading the requirements should be able to get all the information they need
> from one document or from one section of a document. They should not have to
> jump between different sections to understand the requirement. (Patterns for
> Effective Use Cases by Steve Adolph et al., Chapter 7.1)

## Safety

### Safety does not exist without blood, loss or failure

Safety is not there from the very beginning. A gloomy poet could say that safety
blooms on blood. Safety does also not exist on its own: you first need to build
something that kills people or causes a loss, then some people will bother to
learn from this and take actions. Only then safety gets recognized and truly
appreciated.

Consequence: safety is especially sound for those folks who have some experience
of dealing with blood, loss or failure.

### Safety is boring

When implemented well enough, safety becomes boring. Everything is working, no
one complains. At that moment, it is easier than ever to forget about why the
safety is there in the first place. Example: how often do we bother to look at
the safety manuals? Does it mean that the safety is there?

### Safety is very hard to achieve but is very easy to lose

Safety is the extremely fragile and sensitive property of the systems. It so
much effort that is put into achieving it and still it is so easy to let the
whole system get down. Some of the very popular reasons for the failure are:

- degradation of existing components
- changes to the system that do not take the current system's behavior into
  account
- new unexpected factors coming outside the system boundary

Consequence: safety requires continuous and intelligent effort.

### Success breeds failure

Handbook of Walkthroughs, Inspections, and Technical Reviews, p.412:

> ... however, we have to anticipate that we will in fact succeed once in a
> while - and we must also anticipate what that success will bring. For
> instance, one error-riddled system was seldom used by its several hundred
> potential users, so management decided to mount an effort to have the system
> repaired in a systematic fashion. The resulting system was so dependable and
> useful that usage suddenly increased by a factor of a thousand over previous
> usage. This increase in transaction volume made the file design of the system
> completely inadequate to the daily load - which soon meant that nobody could
> get results fast enough to be useful. The entire problem - and so many others
> like it - could have been avoided if the review group had only considered that
> unavoidable law of nature: **Success breeds failure**. So, ..., be prepared
> for the inevitable reaction. If you start making systems better, your users
> will want more of the same - the best side effect of all.

### Safety as a Defensive Discipline

Safety is often seen as a defensive discipline, in contrast to fields focused on
creation, innovation, and action, which drive progress. While these fields push
forward with new ideas and developments, safety functions as a secondary,
backing force. Its role is to prevent harm, minimize risks, and ensure that
these actions happen within a secure framework. Safety doesn't seek to lead the
charge but to protect and enable other processes to unfold without catastrophic
failure.

However, the drive to "lead the charge" often means safety is ignored or
sidelined until it's too late. In this way, safety acts like a belt that holds
uncontrolled progress together, preventing it from falling apart when the
inevitable risks are not properly addressed.

### Safety for Engineering is Like Medicine for People

Medicine isn't the most exciting thing, and no one wants to spend all their time
thinking about it. But it's clear that humanity can't thrive without it, even
with all the amazing achievements of civilization.

In the same way, organizations focus on building things that work and often
don't think much about safety or quality as long as things are fine and
customers are happy. But over time, they may realize that the "health" of their
products, teams, and development processes also matters.

How safety and quality are handled depends a lot on experience and knowledge.
Not long ago, amputation was seen as the best way to treat many illnesses. This
shows how much we've learned and how practices improve over time. Engineering
also needs to grow in this way, moving beyond quick fixes to create stronger,
longer-lasting solutions.

### Understanding as a Prerequisite for Safety Assessment

> Assessing whether a system is safe, requires understanding the system
> sufficiently.

Sources:
[1](https://static.sched.com/hosted_files/eoss24/da/EOSS-ELISA-Enabling-OSS-philipp-ahmann.pdf),
[2](https://lpc.events/event/18/contributions/1896/attachments/1666/3459/LPCMCSafeLinux%2020240920-latest%20Aspects%20of%20Dependable%20Linux%20Systems.pdf)

### User Interfaces and Critical Systems

Too much simplicity can be a problem. Overly simplistic interfaces may prevent
operators from engaging their brains fully, which could negatively impact their
performance in critical situations. If an interface is too simple, operators can
fall into automatism, executing the wrong action due to a lack of alertness.
There are serious concerns that software and interface designers should
prioritize preventing user mistakes, rather than focusing solely on aesthetics.

## Books

- [The Art of Systems Thinking](https://www.google.de/search?q=the+art+of+systems+thinking+book&oq=the+art+of+systems+thinking+book)

## Similar resources

- [Kent Beck - Mastering Programming](https://www.facebook.com/notes/kent-beck/mastering-programming/1184427814923414/)
- [Heuristics of Software Testability](http://www.satisfice.com/tools/testable.pdf)
- [The Law of Leaky Abstractions](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)
- [Lessons Learned in Software Development](https://henrikwarne.com/2015/04/16/lessons-learned-in-software-development/)

## Copyright

Copyright (c) 2015-2025 Stanislav Pankevich s.pankevich@gmail.com.
