# Helix Matrix Traversal

A lightweight Python library that:

- Asynchronously fetches a square numerical matrix from a remote server via HTTP(S).
- Parses the matrix from a custom text format (with borders and separators).
- Returns a `List[int]` containing the result of a **counter-clockwise spiral traversal**, starting from the top-left corner.

This project is a solution to a technical assignment.

---

## Tech Stack

- **Python 3.10+**
- [**httpx**](https://www.python-httpx.org/) - For asynchronous HTTP requests.
- [**pytest**](https://docs.pytest.org/) - For testing.
- [**asyncio**](https://docs.python.org/3/library/asyncio.html) - For asynchronous execution.

---

## Project Structure

```text
helix-matrix/
├── src/
│   └── main.py          # Implementation of get_matrix and spiral logic
├── tests/
│   └── test_main.py     # Unit tests for matrix fetching and traversal
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/helix-matrix.git
cd helix-matrix
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# or
.venv\Scripts\activate           # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Usage

The core functionality is provided by the `get_matrix` function:

```python
import asyncio
from typing import List
from src.main import get_matrix

async def main():
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
    try:
        result: List[int] = await get_matrix(url)
        print(f"Traversed Matrix: {result}")
    except RuntimeError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Function Signature

```python
async def get_matrix(url: str) -> List[int]:
    ...
```

- **Input**: A URL string pointing to a text-formatted matrix.
- **Output**: A list of integers representing the counter-clockwise spiral traversal starting from the top-left element.

### Input Format Requirements

The library expects a square matrix formatted with `+`, `-`, and `|` characters, for example:

```text
+----+----+----+----+
| 10 | 50 | 90 |130 |
+----+----+----+----+
|140 |150 |160 |120 |
+----+----+----+----+
| 80 | 40 | 30 | 20 |
+----+----+----+----+
| 60 |100 |110 | 70 |
+----+----+----+----+
```

The parser automatically:
1. Removes formatting characters and whitespace.
2. Extracts numerical values.
3. Validates the structure before traversal.

---

## Error Handling

Network interactions are managed using `httpx.AsyncClient` and wrapped in robust error handling:

- **Server Errors (4xx/5xx)**: Raises `RuntimeError("Server error: ...")`.
- **Network Issues (Timeout, Connection Refused)**: Raises `RuntimeError("Network error: ...")`.

This ensures that the calling code can handle failures gracefully.

---

## Running Tests

To verify the implementation, run the following command:

```bash
pytest
```

The tests cover:
- Successful asynchronous data fetching.
- Correct parsing of the text-based matrix format.
- Accuracy of the counter-clockwise spiral traversal algorithm.
