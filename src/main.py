import re
from typing import List
import httpx


async def get_matrix(url: str) -> List[int]:
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url, timeout=10.0)
            res.raise_for_status()
            
            result = get_matrix_from_text(res)
            
            return spiral(result)
        
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(f"Server error: {exc}") from exc
        
        except httpx.RequestError as exc:
            raise RuntimeError(f"Network error: {exc}") from exc

def get_matrix_from_text(res):
    lines = res.text.split('\n')
    result = []
    for line in lines:
        if numbers := re.findall(r'\d+', line):
            result.append([int(x) for x in numbers])
    return result


def spiral(matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(matrix)
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1

        for j in range(left, right + 1):
            result.append(matrix[bottom][j])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][right])
        right -= 1

        for j in range(right, left - 1, -1):
            result.append(matrix[top][j])
        top += 1

    return result