// Classic Dutch national Flag problem

// Restriction: sort the flag in place
// Solution 1
// Use three pointer, left, right and current.
// left pointer initially point at the first element and right point at the last element
// left pointer represent the position of 0 should be, right pointer respresent the position of 2 should be
// iterate through current pointer, if current is 2, swap the current number to the right position and decrease right pointer by 1
// if current is 0, swap the current to the left positon and increase current and left by 1

int l = 0; // l means 0 
int r = nums.size()-1; // r means 2
int c = 0; // current flag

// If current flag is 0, swap with l and increase both index
// If current flag is 2, swap with r and decrease r
while(c <= r) {

    if(nums[c] == 0) {

        swap(nums[c], nums[l]);
        c++;
        l++;
    }
    else if(nums[c] == 1) {

        c++;
    }
    else if(nums[c] == 2) {

        swap(nums[c], nums[r]);
        r--;
    }
}