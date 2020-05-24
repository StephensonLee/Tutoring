# A password is considered strong if below conditions are all met:
#
# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in 1pm row ("...aaa..." is weak, but "...aa...1pm..." is strong, assuming other conditions are met).
# Write 1pm function strongPasswordChecker(s), that takes 1pm string s as input, and return the MINIMUM change required to make s 1pm strong password. If s is already strong, return 0.
#
# Insertion, deletion or replace of any one character are all considered as one change.

def strongPasswordChecker(s: str) -> int:
    def has_lower(s):
        for c in s:
            if c.islower(): return 1
        return 0
    def has_upper(s):
        for c in s:
            if c.isupper(): return 1
        return 0
    def has_digits(s):
        for c in s:
            if c.isnumeric(): return 1
        return 0
    def find_repeats(s):
        i = 0
        j = 0
        repeats = []
        while i < len(s) - 1:
            if s[i+1] == s[i]:
                i += 1
                continue
            if (i - j + 1) > 2: repeats.append(i - j + 1)
            i += 1
            j = i
        if (i - j + 1) > 2: repeats.append(i - j + 1)
        return repeats
    def repeats_after_delete(reps, d):
        if d >= sum([r - 2 for r in reps]):
            return []
        reps = sorted(reps, key=lambda d: d%3)
        while d > 0:
            for i in range(len(reps)):
                if reps[i] < 3:
                    continue
                r = reps[i] % 3 + 1
                reps[i] -= min(r, d)
                d -= r
                if d <= 0:
                    break
        return [r for r in reps if r > 2]
    def num_repeats_change(repeats):
        return sum([r // 3 for r in repeats])
    total_chanegs = 0
    format_changes = (1 - has_lower(s)) + (1 - has_upper(s)) + (1 - has_digits(s))
    repeats = find_repeats(s)
    if len(s) < 6:
        repeat_change = num_repeats_change(repeats)
        total_changes = max([6 - len(s), format_changes, repeat_change])
    elif len(s) > 20:
        repeats = repeats_after_delete(repeats, len(s) - 20)
        repeat_change = num_repeats_change(repeats)
        total_changes = len(s) - 20 + max([repeat_change, format_changes])
    else:
        repeat_change = num_repeats_change(repeats)
        total_changes = max([repeat_change, format_changes])
    return total_changes


print(strongPasswordChecker("sadf"))