package leetcodeproblems

import (
	"fmt"
	"math"
)

func ReverseInteger(x int) int {

	//int32能表示的整数范围[-2^31,2^31-1]
	var i int32 = 2147483647
	fmt.Printf("%d\n", i)   //2^31-1
	fmt.Printf("%d\n", i+1) //-2^31
	fmt.Printf("%d\n", i+2) //-2^31 + 1

	//正整溢出的时候, 如果步长比较大,那么溢出之后仍然可能为整数
	i = 964632435
	fmt.Printf("%d\n", i) //964632435
	i *= 10
	fmt.Printf("%d\n", i) //1056389758
	fmt.Println()

	//golang中取余运算的结果的正负号和第一个操作数正负号相同
	//所以, 如果 x < 0, 那么digit和result都小于零
	result := 0
	for x != 0 {
		if result < math.MinInt32/10 || result > math.MaxInt32/10 {
			return 0
		}
		digit := x % 10
		x /= 10
		result = result*10 + digit
	}
	return result
}
