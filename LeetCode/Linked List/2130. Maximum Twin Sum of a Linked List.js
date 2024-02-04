//  Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val
  this.next = next === undefined ? null : next
}
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function (head) {
  const nodeVals = []
  while (head) {
    nodeVals.push(head.val)
    head = head.next
  }
  let maxPair = 0
  const n = nodeVals.length
  for (let i = 0; i <= Math.floor(n / 2) - 1; i++) {
    maxPair = Math.max(maxPair, nodeVals[i] + nodeVals[n - i - 1])
  }
  return maxPair
}
