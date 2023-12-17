package pkg

//参考https://pkg.go.dev/golang.org/x/exp/constraints

type SignedInteger interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64
}

type UnsignedInteger interface {
	~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr
}

type Float interface {
	~float32 | ~float64
}

type Ordered interface {
	SignedInteger | UnsignedInteger | Float | ~string
}

func Max[operand Ordered](a, b operand) operand {
	if b > a {
		return b
	}
	return a
}

func Min[operand Ordered](a, b operand) operand {
	if b < a {
		return b
	}
	return a
}
