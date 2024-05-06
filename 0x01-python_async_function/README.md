# Async and Await Syntax

In Python, the `async` and `await` keywords are used to define and work with asynchronous functions, also known as coroutines. These keywords were introduced in Python 3.5 and provide a more readable and straightforward way to write asynchronous code compared to using callbacks or low-level event loops.

## How to Execute an Async Program with AsyncIO

The `asyncio` module in Python is the standard library for writing concurrent code using the async/await syntax. It provides a set of high-level APIs for creating and managing asynchronous tasks, handling I/O operations, and more.

Here's an example of how to execute an async program with `asyncio`:

```python
import asyncio

async def main():
    print("Hello, World!")

asyncio.run(main())
