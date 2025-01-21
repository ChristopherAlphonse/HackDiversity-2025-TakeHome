
# Hack Diversity Fellow Technical Interview: Accessible Route Search and Sorting Challenge

### Overview
This technical challenge assesses your understanding of beginner-level data structures and algorithms with a real-world application focused on accessibility. You’ll create an algorithm that filters and sorts accessible routes and submit your solution through a RESTful API and GitHub.

---

### Objectives
This exercise evaluates the following key skills:
- **Data Structures**: Use arrays or linked lists.
- **Algorithms**: Implement linear search and a sorting algorithm (e.g., bubble sort, selection sort, or insertion sort).
- **API Interaction**: Retrieve and submit data via a RESTful API.
- **Version Control**: Use GitHub to submit your code with frequent commits.

---

### Language and Requirements

- **Preferred Language**: Complete the challenge in any language you’re comfortable with, as long as it enables you to:
  - Implement linear search and basic sorting algorithms.
  - Interact with RESTful APIs using `GET` and `POST` requests.
  - Use version control with Git and push code to GitHub.

- **Requirements**: Ensure your solution meets the following criteria:
  - Filters accessible routes using linear search.
  - Sorts routes by distance in ascending order using a basic sorting algorithm (bubble sort, selection sort, or insertion sort).
  - Submits a sorted list of routes to the API as specified.

---

### Preparation and Setup

1. **Create a New Private Repository**
   - Log in to your GitHub account.
   - Click on the "+" sign in the top-right corner and select **New repository**.
   - Name your repository appropriately (e.g., `HackDiversity-2025-TakeHome`).
   - Ensure the repository visibility is set to **Private**.

2. **Clone and Push**
   - Clone the original repository to your local machine using the provided link (`git clone` command).
   - Push the cloned content to your newly created private repository.

3. **Add Hack.Diversity as a Collaborator**
   - Navigate to your new private repository on GitHub.
   - Click on the **Settings** tab.
   - In the left menu, select **Collaborators and teams**.
   - Click **Add people** and invite the GitHub account `HackDotDiversity` as a collaborator.

4. **Time Allocation**
   - This challenge should take 30–45 minutes, including implementation, testing, and GitHub submission.

---

## Starting a New Session

To begin the interview, create a unique session. Follow these steps to initialize your session and retrieve a `session_id`, which you will use for authorization in subsequent API requests.

### Endpoint: `/api/start-session`
- **Method**: `POST`
- **Description**: Initializes a new session and returns a unique `session_id` required for authentication in subsequent requests.

### Request Body (JSON)
```json
{
    "firstName": "YourFirstName",
    "lastName": "YourLastName"
}
```

| Field     | Type   | Description          |
| --------- | ------ | -------------------- |
| firstName | string | Your first name      |
| lastName  | string | Your last name       |

### Response
If the session is created successfully, the response will include a unique `session_id` for use as a Bearer token in the Authorization header for other endpoints.

```json
{
    "session_id": "your-unique-session-id"
}
```

### Example in [Postman](https://medium.com/assertqualityassurance/rest-api-test-automation-with-postman-jenkins-1-of-3-860edf3c2a45)
1. Select the `POST` method.
2. Enter the URL: `https://hackdiversity.xyz/api/start-session`
3. Add the following JSON to the request body:

    ```json
    {
        "firstName": "Jean-Jacques", //Input Your First Name
        "lastName": "Dessalines" //Input Your Last Name
    }
    ```

4. Send the request.
5. Copy the `session_id` from the response and use it as your Bearer token in the Authorization header for all subsequent API requests.

### Authorization Header Format
Once you have your `session_id`, include it in the Authorization header for all API requests that require authentication.

```plaintext
Authorization: Bearer <session_id>
```

Replace `<session_id>` with the unique session ID received from the `/api/start-session` endpoint.

---

## The Task

### 1. Retrieve Route Data
- **URL**: `https://hackdiversity.xyz/api/navigation/routes`
- **Method**: `GET`
- **Authorization**: Include the `session_id` as a Bearer token in the Authorization header.

### 2. Algorithm Requirements
- **Filter**: Include only accessible routes from the data.
- **Sort**: Arrange the filtered routes by distance in ascending order using one of the following:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort

### 3. Test and Validate
- Retrieve sample data from `https://hackdiversity.xyz/api/test/mockRoutes` to test your algorithm.
- Submit test data to `https://hackdiversity.xyz/api/test/submit-sorted-routes` to validate your logic (up to 3 attempts available, which do not impact your final submission count).

### 4. Submit Final Routes
- **Final Submission URL**: `https://hackdiversity.xyz/api/navigation/sorted_routes`
- **Attempts**: Up to 10 attempts are allowed, each of which is logged for review.

### 5. Completion Status
- **Check Progress**: 
  - **URL**: `https://hackdiversity.xyz/api/navigation/status`
  - **Method**: `GET`
  - This will display your progress, remaining attempts, and feedback on prior submissions.

---

### Submission Instructions

- In addition to completing the challenge in your **private repository** and adding `HackDotDiversity` as a collaborator:
  - Submit a **zip file** containing your code to the following link:  
    [Submit Here](https://forms.gle/2zby2Pia3BR4e2na7).

---

### Helpful Tips

- **Algorithm Hints**: Use linear search for filtering and simple sorting algorithms for ordering routes.
- **Validate Locally**: Test locally to reduce API submission errors.
- **Use Version Control**: Commit regularly with meaningful messages.

---

### Evaluation Criteria

Your submission will be evaluated on correctness, code quality, completion, and efficiency. Showcase your problem-solving and technical skills—GOOD LUCK👾!
