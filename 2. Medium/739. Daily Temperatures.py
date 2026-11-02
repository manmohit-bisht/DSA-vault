class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n):
            while (
                st and temperatures[st[-1]] < temperatures[i]
            ):  # if the current temperature is greater than the temperature at the index stored at the top of the stack, we have found a warmer day for the day at index st[-1]
                waited_days = i - st[-1]
                ans[st[-1]] = waited_days
                st.pop()
            st.append(i)
        return ans
