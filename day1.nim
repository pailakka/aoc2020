import strutils
import sequtils

let input = @"""1721
            979
            366
            299
            675
            1456""".split("\n")

let numbers = input.map(r => r.strip())

echo numbers