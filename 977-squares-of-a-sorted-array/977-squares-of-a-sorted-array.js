/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let negativePivot = nums.length - 1, positivePivot = 0;
    for(let i = 0; i < nums.length; i++){
        if (nums[i] >= 0){
            positivePivot = i;
            negativePivot = i-1;
            break;
        }
    }
    
    const res = [];
    if(negativePivot === nums.length - 1) return nums.map(num => num*num).reverse()
    if(positivePivot === 0) return nums.map(num => num*num)
    
    while(negativePivot >= 0 && positivePivot < nums.length){
        negNum = nums[negativePivot] * nums[negativePivot]
        posNum = nums[positivePivot] * nums[positivePivot]
        if(posNum <= negNum){ 
            res.push(posNum);
            positivePivot++;
        } else {
            res.push(negNum);
            negativePivot--;
        }           
    }
    
    while(negativePivot >= 0){
        res.push(nums[negativePivot]*nums[negativePivot])
        negativePivot--;
    }
    
    while(positivePivot < nums.length){
        res.push(nums[positivePivot]*nums[positivePivot])
        positivePivot++;
    }
    
    return res;
};