class Solution:
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        # What characters do we need?
        need_count = {}

        for ch in t:
            need_count[ch] = need_count.get(ch, 0) + 1

        # Characters inside current window
        window = {}

        have = 0
        need = len(need_count)

        left = 0

        best_len = float("inf")
        best_left = 0

        for right in range(len(s)):

            ch = s[right]

            # Add character to window
            window[ch] = window.get(ch, 0) + 1

            # Did we just satisfy a required character?
            if ch in need_count and window[ch] == need_count[ch]:
                have += 1

            # Window is valid
            while have == need:

                # Check if this is the smallest window
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                # Remove left character
                left_ch = s[left]

                window[left_ch] -= 1

                # Did removing it make the window invalid?
                if left_ch in need_count and \
                   window[left_ch] < need_count[left_ch]:

                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_left + best_len]