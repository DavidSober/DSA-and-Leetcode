#include <iostream>
#include <iterator>  // For std::size

int main() {

    // we ca declare a static array like so
    int nums[3];
    nums[0] = 1; // then define it here
    nums[1] = 2;
    nums[2] = 3;

    std::cout << "test " << nums[0] << "other elements in nums are: \n" << std::endl;
    int size = sizeof(nums) / sizeof(nums[0]);

    std::cout << "len of arr called nums is: " << size << std::endl;

    for (int i = 0; i < size; i++) {
        std::cout << nums[i] << std::endl;   
    }

    int nums2[] = {1, 2, 3, 4}; // we can also define it faster like so
    int sizeofnums2 = sizeof(nums2) / sizeof(nums2[0]);
    for (int i = 0; i < sizeofnums2; i++) {
        std::cout << nums2[i] << std::endl;
    }
    std::cout << "size of nums2 is: " << sizeofnums2 << std::endl;
}

