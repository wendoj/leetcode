# LeetCode Solutions

My solutions to [LeetCode](https://leetcode.com) problems, committed automatically each time I get an
**Accepted** verdict. This repo is my running record of practice: data structures, algorithms, and
problem-solving patterns.

## Progress

<!-- STATS:START -->
**9 solved**  ·  Easy: 7  ·  Medium: 2

**Languages:** Python (9)

| # | Problem | Difficulty | Solution |
|--:|---------|:----------:|----------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](easy/0001-two-sum.py) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | [Python](easy/0020-valid-parentheses.py) |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [Python](medium/0049-group-anagrams.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | [Python](easy/0125-valid-palindrome.py) |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | [Python](easy/0217-contains-duplicate.py) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | [Python](easy/0242-valid-anagram.py) |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [Python](medium/0347-top-k-frequent-elements.py) |
| 1523 | [Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | Easy | [Python](easy/1523-count-odd-numbers-in-an-interval-range.py) |
| 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | [Python](easy/1929-concatenation-of-array.py) |
<!-- STATS:END -->

## How this repo is organized

- Files are named `<problem number>-<problem-slug>.<ext>`, so they sort in LeetCode order and the
  slug matches the problem's URL.
- Solutions are grouped into `easy/`, `medium/`, and `hard/` folders.
- Each file starts with a short comment header: the problem title, difficulty, a link, and the
  runtime and memory from the accepted submission.
- Where a problem is solved in more than one language, each version sits side by side.

## How solutions get here

A browser extension watches for an accepted submission and commits the code to this repo through
the GitHub API, so there's no manual copy-and-paste.

## Keeping this README current

The progress table above is generated from the files in the repo by `scripts/update_readme.py`.
A GitHub Action (`.github/workflows/update-readme.yml`) re-runs it after every push and commits the
updated table. To refresh it by hand: `python3 scripts/update_readme.py`.

## Notes

- Solutions are my own attempts at the time of submission. Some aren't optimal, and I'm happy to
  revisit them as I learn more.
- If you're working through the same problems, try them yourself first. Reading solutions teaches far
  less than struggling with the problem.
