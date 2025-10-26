# Todo Application Requirements

## Functional Requirements

1. **UI Structure**: The application needs to include a title, a form for entering new tasks (with input field and add button), and a list for displaying todo items.

2. **Design Style**: Design a modern, clean CSS style. The main content should be centered with a maximum width of 800px. Input fields and buttons should be aesthetically pleasing. List items should have spacing between them. Buttons and list items should have visual feedback effects on hover.

3. **Add Todo Function**: When the user clicks the add button, get the content from the input field, create a new `<li>` element and add it to the list, then clear the input field.

4. **Complete and Delete Functions**: Each list item (`<li>`) should include a 'Complete' button and a 'Delete' button. Clicking the 'Complete' button should add a 'completed' CSS class (for striking through text). Clicking the 'Delete' button should remove the list item from the list.

5. **Filter and Clear Functions**: Implement filter options including "All", "Active", and "Completed". Bottom functions should include "Clear Completed" and "Clear All".

## Technical Requirements

- **Frontend**: React
- **Backend**: FastAPI
- **Database**: SQLite

## Project Structure

- Project divided into: `backend` and `frontend` directories

## Database Design

Design a database table for the todo application and provide SQL statements.
