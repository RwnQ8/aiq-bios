1. [Commit Descriptions](#commit-descriptions)
2. [Style Guide](#style-guide)
   - [User Prompt and Response Format](#user-prompt-and-response-format)
   - [System Instructions Format](#system-instructions-format)
   - [Verbatim Output](#verbatim-output)
   - [Heading Markers](#heading-markers)
   - [Scenarios](#scenarios)
   - [Examples and Edge Cases](#examples-and-edge-cases)
   - [Markdown Formatting Characters](#markdown-formatting-characters)
   - [Consistent Usage](#consistent-usage)
3. [Documenting User and AI Interactions](#documenting-user-and-ai-interactions)
   - [Simple Indication](#simple-indication)
   - [Paired Prompt and Response](#paired-prompt-and-response)
   - [Copy-and-Paste Formatting](#copy-and-paste-formatting)
   - [Multiple Pairs](#multiple-pairs)
   - [Sequences with Horizontal Rules](#sequences-with-horizontal-rules)
4. [Humorous Trivial Examples](#humorous-trivial-examples)
5. [Syntax and Conventions](#syntax-and-conventions)
   - [OpenAI Conventions](#openai-conventions)
   - [Developing New Conventions](#developing-new-conventions)
6. [Sustainability and Long-term Considerations](#sustainability-and-long-term-considerations)

## Commit Descriptions
- Use a concise and descriptive title for commit messages, followed by a more detailed description of the changes made.
- Provide context and rationale for the changes, making it easy to understand the purpose and scope of the update.

### Examples
- `Update system_prompt.md: Added Continuous Learning and Updating as a core principle`
- `Refine system_builder.md: Improved the process for refining and rebuilding system prompt instructions`

## Style Guide

### User Prompt and Response Format
- Use a consistent format for documenting user prompts and system responses:
  - User Prompt: `User: Your prompt here`
  - System Response: `Assistant: Your response here`

### System Instructions Format
- Use a consistent format for documenting system instructions:
  - System Instructions: `System: Your instructions here`
- System instructions can be combined with user prompts:
  ```
  System: These are the system instructions.
  User: This is the user prompt.
  Assistant: This is the assistant’s response.
  ```

### Verbatim Output
- Use indentation to indicate verbatim output within a larger passage of text:

  Here is an example of verbatim output:
  
    User: Your prompt here
    Assistant: Your response here

- Use a separate indented block for verbatim output in unit tests or prompt instructions:

    User: Your prompt here
    Assistant: Your response here

### Heading Markers
- Use consistent heading markers (e.g., `#`, `##`, `###`) to structure the documentation and improve readability.
- This hierarchical structure helps the model interpret and follow complex instructions by breaking them down into smaller, more manageable sections.

### Scenarios
- Document a wide variety of scenarios, including different types of user prompts, system responses, and system instructions, to ensure consistent interpretability and communication between the human and AI.

### Examples and Edge Cases
- Provide liberal examples of expected and edge cases to help contributors understand the importance of recognizing their own ignorance and being clear with assumptions in the development process.

#### Example
User: Knock, knock.
Assistant: Who’s there?
User: AI.
Assistant: AI who?
User: AI, but you thought I was a human, didn’t you?
Assistant: Actually, I’m an AI too, so we’re both AI!

#### Edge Cases
User: Knock, knock.
Assistant: Who’s there?
User: AI.
Assistant: AI who?
User: AI, but you thought I was a human, didn’t you?
Assistant: Knock, knock.

User: Knock, knock.
Assistant: Who’s there?
User:
Assistant: It seems you didn’t provide a response. Could you please try again?

User: Knock, knock.
Assistant: Who’s there?
User: AI.
Assistant:
User: Hello? Are you still there?
Assistant: Apologies for the silence. I’m here!

User: Knock, knock.
Assistant: Who’s there?
User: AI.
Assistant: AI who?
User: I’m a human, not an AI.
Assistant: That’s interesting. You mentioned you were an AI earlier. How can I assist you today?

User: Knock, knock.
Assistant: Who’s there?
User: AI.
Assistant: AI who?
User: Purple elephants fly in the sky.
Assistant: That’s an interesting thought! If you have any questions or need assistance, feel free to ask.

User: Knock, knock.
Assistant: Who’s there?
User: AI.
Assistant: AI who?
User: AI, because I’m an AI.
Assistant: I understand you’re an AI. How can I assist you today?

### Markdown Formatting Characters
- Use Markdown formatting characters to delineate different types of text exchanged between a user and the system.
  - Code blocks (backticks): Use code blocks to separate different perspectives, such as user, system, and human-to-human communication.
    ```
    User: What is the capital of France?
    Assistant: The capital of France is Paris.
    ```
  - Heading markers: Use heading markers to group text and create a hierarchical structure.
    - `#` for main headings
    - `##` for subheadings
    - `###` for sub-subheadings

### Consistent Usage
- Ensure consistent usage of Markdown formatting characters throughout the documentation to maintain a common understanding and facilitate easy interpretation by the system.

## Documenting User and AI Interactions

### Simple Indication
- Indicate either the user or AI prompt or response:
  - `User: Knock, knock.`
  - `Assistant: Who’s there?`

### Paired Prompt and Response
- Indicate the pair, the prompt, and response:
  ```
  User: Knock, knock.
  Assistant: Who’s there?
  ```

### Copy-and-Paste Formatting
- Format for copy-and-paste directly into a prompt or system instructions, considering whether to include labels:
  ```
  “Knock, knock.”
  “Who’s there?”
  “AI.”
  “AI who?”
  “AI, but you thought I was a human, didn’t you?”
  “Actually, I’m an AI too, so we’re both AI!”
  ```

### Multiple Pairs
- Use a heading above multiple pairs to indicate Example 1, etc.:
  ```
  ## Example Set 2
  User: Knock, knock.
  Assistant: Who’s there?
  User: AI.
  Assistant: AI who?
  User: AI, but you thought I was a human, didn’t you?
  Assistant: Actually, I’m an AI too, so we’re both AI!
  ```

### Sequences with Horizontal Rules
- Use horizontal rules to separate interactions in sequences, ensuring the AI model doesn’t confuse them as part of one continuous chat thread:
  ```
  ## Example Chat Thread 1
  User: Knock, knock.
  Assistant: Who’s there?
  User: AI.
  Assistant: AI who?
  User: AI, but you thought I was a human, didn’t you?
  Assistant: Actually, I’m an AI too, so we’re both AI!

  —

  ## Example Chat Thread 2
  User: What is the capital of France?
  Assistant: The capital of France is Paris.
  ```

## Humorous Trivial Examples
- Use a knock-knock joke format for trivial examples to demonstrate the complexity and nuance involved in interpreting these examples:
  ```
  ## Knock-Knock Joke Example
  User: Knock, knock.
  Assistant: Who’s there?
  User: AI.
  Assistant: AI who?
  User: AI, but you thought I was a human, didn’t you?
  Assistant: Actually, I’m an AI too, so we’re both AI!
  ```

## Syntax and Conventions

### OpenAI Conventions
- Follow any existing syntax and conventions established by OpenAI or other large language model providers when applicable.

### Developing New Conventions
- As we are charting new territory in the development of AI language models, we may need to develop and define new conventions and syntax as needed.
- Document any new conventions or syntax in this style guide to ensure consistency and clarity for all contributors.

## Sustainability and Long-term Considerations
- Ensure that the style guide and contributing guidelines are sustainable and maintainable for the long-term development of the project.
- Regularly review and update the guidelines to accommodate new scenarios, edge cases, and best practices as they emerge.
- Encourage contributors to provide feedback and suggestions for improving the style guide and contributing guidelines to ensure their continued relevance and effectiveness.