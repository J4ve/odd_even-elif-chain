# Odd/Even Elif Chain

A community-powered odd/even checker where every contributor adds exactly **one number**.  
This project brute-forces odd/even detection with an endlessly growing chain of `if` / `elif` statements.  
It is intentionally the most inefficient way to solve a trivial problem.  

---

## How It Works
- The program determines if a number is odd or even by walking through thousands of `if` / `elif` lines.  
- Each contributor adds **one `elif` block** for a single number.  
- Together, the community builds the longest odd/even checker ever attempted.  

Example:

```python
if num == 1:
    print("odd") # Added by 
elif num == 2:
    print("even")
elif num == 3:
    print("odd")
# ...and so on
```

---

## Contribution Rules
1. You may only add **one number per pull request**.  
2. Follow this format exactly:  

   ```python
   elif num == YOUR_NUMBER:
       print("odd")  # or "even"  # Added by YOUR-GITHUB-USERNAME
   ```
   Example:
  ```python
    elif num == 10:
        print("even")  # Added by @J4ve
  ```

4. Insert your line in the correct order (ascending).  
5. Do not edit or remove other contributors’ numbers.  
6. No bots or automation. This is a human-only effort.  

---

## Running the Program
```bash
python main.py
```

The script asks for a number and checks it against the massive `if/elif` chain.  

---

## Why?
Why not??

---

## Goals
- [X] Create this repo
- [ ] Reach 100 numbers
- [ ] Reach 500 numbers
- [ ] Reach 1,000 numbers  
- [ ] Reach 10,000 numbers  
- [ ] Hit GitHub limits  

---

## How to Contribute (Pull Request Tutorial)

If this is your first time contributing to open source, follow these steps:

1. **Fork this repository**  
   Click the "Fork" button at the top right of this page to make a copy under your GitHub account.  

2. **Clone your fork**  
   Open a terminal and run:  
   ```bash
   git clone https://github.com/J4ve/odd_even-elif-chain.git
   cd odd_even-elif-chain
   ```

3. **Create a new branch**  
   ```bash
   git checkout -b add-number-XYZ
   ```
   Replace `XYZ` with your number.  

4. **Edit `main.py`**  
   Add your `elif` statement in the correct spot (ascending order).  

5. **Commit your change**  
   ```bash
   git add main.py
   git commit -m "Add number XYZ"
   ```

6. **Push to your fork**  
   ```bash
   git push origin add-number-XYZ
   ```

7. **Open a Pull Request**  
   Go to your fork on GitHub, and click the "Compare & pull request" button.  
   Submit your PR and wait for it to be reviewed/merged.

### Still new to open source? Check this beginner-friendly guide:  
[First Contributions](https://github.com/firstcontributions/first-contributions)


