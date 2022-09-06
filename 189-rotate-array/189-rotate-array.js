/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var reverse = function(arr, s, e){
    while(s < e){
        let temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp
        s++
        e--
    }
}

var rotate = function(nums, k) {
    r = k % nums.length
    reverse(nums, 0, nums.length - r - 1)
    reverse(nums, nums.length - r, nums.length - 1)
    reverse(nums, 0, nums.length - 1)
    return nums
};