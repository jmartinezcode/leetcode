// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// getMin() -- Retrieve the minimum element in the stack.
 

// Example:

// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin();   --> Returns -3.
// minStack.pop();
// minStack.top();      --> Returns 0.
// minStack.getMin();   --> Returns -2.
 
public class MinStack
{
    Stack<int> stack = new Stack<int>();
    int min = int.MaxValue;

    public void Push(int x)
    {
        if (x <= min)   //push old min value only when current min changes after pushing new x
        {
            stack.Push(min);
            min = x;
        }
        stack.Push(x);
    }

    public void Pop()
    {
        if (stack.Pop() == min)
            min = stack.Pop();
    }

    public int Top() => stack.Peek();
    public int GetMin() => min;
}