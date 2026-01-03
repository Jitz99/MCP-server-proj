from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply(a:float,b:float)-> float:
    """Multiply two numbers
    
    args: a (float): The first number.
          b (float): The second number.
    
    returns: float: The product of the two numbers.
    """
    return a*b

@app.post("/Add")
def add_numbers(x: float,y:float)->float:
    """Add two numbers
    
    args: x (float): The first number.
          y (float): The second number.

    returns: float: The sum of the two numbers.
    """
    return x + y
@app.post("/substract")
def subtract(a: float, b: float) -> float:
    """Subtract two numbers
    
    args: a (float): The first number.
          b (float): The second number.
    
    returns: float: The result of a minus b.
    """
    return a - b
@app.post("/divide")
def divide(a: float, b: float) -> float:
    """Divide two numbers
    
    args: a (float): The numerator.
          b (float): The denominator.
    
    returns: float: The result of a divided by b.
    
    raises: ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

mcp=FastApiMCP(app,name="Calculator MCP")
mcp.mount()

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8002)