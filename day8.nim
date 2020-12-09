import strutils
import sequtils, sugar
import algorithm
import times, os
import sets

let input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

type
  Operation = tuple[instruction: string, param: int]

proc flipOperation(op: Operation): Operation =
  let flipped = (if op.instruction == "jmp": "nop" else: "jmp")
  return (instruction: flipped, param: op.param)

let time = cpuTime()
var instructions: seq[Operation]

instructions = toSeq(input.split("\n")).map(x => x.strip().split(' ')).map(x => (instruction: x[0], param: parseInt(x[1])))

var oldops = initHashSet[int]()

proc applyOp(op: Operation, i: int, nval: int): (int,int) =
    if op[0] == "nop":
      i = i+1
    elif op[0] == "jmp":
      i = i+op[1]
    elif op[0] == "acc":
      nval = nval + op[1]
      i = i+1
    else:
      echo "VPS"
    
    return (i, nval)

proc runOperations(ops: seq[Operation], starti: int, val: int, firstOperation: Operation): int =
  var i = starti
  var nval = val

  if not isNil(firstOperation):
    let opvals = applyOp(firstOperation, i,nval)
    i = opvals[0]
    nval = opvals[1]

  while i < ops.len():
    let op = ops[i]
    if op[0] == "nop" or op[0] == "jmp":
      let ret = runOperations(ops,i+1,nval,op.flipOperation())
      if ret != -1:
        return ret

    let opvals  = applyOp(op, i,nval)
    
    if oldops.contains(i):
      return -1
    oldops.incl(i)

  return nval

debugEcho runOperations(instructions, 0, 0, nil)

echo "Time taken: ", cpuTime() - time