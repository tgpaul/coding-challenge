# Coding Challenge Guidelines

Please organize, design, test, document and make your code deployment ready as if it was going into production.

## Functional requirement

Create a service that tells the user what types of food options might be found near a specific location on a map.
As a user, I want to list all restaurants in my city - Sorted by rating - Filters -> Has table booking - Has online delivery - Cusines

The data is available in the data folder

## Technical requirement

We believe there is no one-size-fits-all technology. Good engineering is about
using the right tool for the right job, and constantly learning about them.
Therefore, feel free to mention in your `README` how much experience you have
with the technical stack you choose, we will take note of that when reviewing
your challenge.

Here are some technologies we love:

- Java
- Python
- JavaScript
- Ruby
- Rust
- Go

You are also free to use any web framework. If you choose to use a framework
that results in boilerplate code in the repository, please detail in your
README which code was written by you (as opposed to generated code).

When you’re done, host it in your local machine. The endpoints must be accessable from within the network. The deployable must be a turnkey solution, which can be deployed on a new server with minimal effort.

## Existing code

If you have existing code, please follow the following guidelines:

- Include a link to the hosted repository (e.g. Github, Bitbucket...). We do not review archives or single files.
- The repo should include a README. In particular, please make sure to include high-level explanation about what the code is doing.
- Ideally, the code you're providing:
  - Has been written by you alone. If not, please tell us which part you wrote and are most proud of in the README.
  - Is leveraging the technologies we embrace.
  - Is deployed and hosted somewhere.

## Readme

Regardless of whether it's your own code or our coding challenge, write your README as if it was for a production service. Include the following items:

- Description of the problem and solution.
- Whether the solution focuses on back-end, front-end or if it's full stack.
- Reasoning behind your technical choices, including architectural.
- Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.
- Link to to the hosted application if applicable.

## How we review

Your application will be reviewed by at least three of our finest.

**We value quality over completeness**. It is fine to leave things aside provided you call them out in your project's README. The goal of this code sample is to help us identify what you consider production-ready code. You should consider this code ready for final review with your colleague, i.e. this would be the last step before deploying to production.

We will be evaluating the following:

- **Architecture**
- **Clarity**
- **Correctness**: does the application do what was asked? If there is anything missing, does the README explain why it is missing?
- **Code quality**: is the code simple, easy to understand, and maintainable? Are there any code smells or other red flags? Does object-oriented code follows principles such as the single responsibility principle? Is the coding style consistent with the language's guidelines? Is it consistent throughout the codebase?
- **Security**: are there any obvious vulnerability?
- **Testing**: Is the application well tested? Are edge cases and corner cases considered and handled?
- **UX**: Are the APIs intuitive?
- **Technical choices**: does choices of libraries, databases, frameworks etc. seem appropriate for the application?

Bonus point (those items are optional):

- **Scalability**: will technical choices scale well? If not, is there a discussion of those choices in the README?
- **Production-readiness**: does the code include monitoring? logging? proper error handling?
