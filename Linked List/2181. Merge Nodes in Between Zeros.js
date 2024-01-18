// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val
  this.next = next === undefined ? null : next
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var mergeNodes = function (head) {
  const merged = new ListNode()
  let current = merged
  let sum = 0
  while (head) {
    if (head.val === 0 && sum != 0) {
      const node = new ListNode(sum)
      sum = 0
      current.next = node
      current = current.next
    } else {
      sum += head.val
    }
    head = head.next
  }
  return merged.next
}
