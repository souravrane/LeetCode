/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
    arr.sort((a,b)=> a - b)

    function binarySearch(target, index){
        let left = 0, right = arr.length - 1
        while(left <= right) {
            const mid = left + Math.floor((right - left) / 2)   
            if(mid !== index && arr[mid] === target) return true
            
            if(arr[mid] < target) left = mid + 1
            else right = mid - 1
        }
        
        return false
    }
    
    let check = false
    arr.forEach( (num, index) => {
        check = check || binarySearch(num * 2, index)
    })
    return check
};