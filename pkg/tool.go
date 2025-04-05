package pkg

import "iter"

// https://go.dev/blog/range-functions#iterating-on-iterators

func Filter[V any](filterFunc func(V) bool, s iter.Seq[V]) iter.Seq[V] {
	return func(yield func(V) bool) {
		for v := range s {
			if filterFunc(v) {
				if !yield(v) {
					return
				}
			}
		}
	}
}

func Map[V1, V2 any](mapFunc func(V1) V2, s iter.Seq[V1]) iter.Seq[V2] {
	return func(yield func(V2) bool) {
		for v1 := range s {
			v2 := mapFunc(v1)
			if !yield(v2) {
				return
			}
		}
	}
}

func Filter2[K, V any](filterFunc func(K, V) bool, s iter.Seq2[K, V]) iter.Seq2[K, V] {
	return func(yield func(K, V) bool) {
		for k, v := range s {
			if filterFunc(k, v) {
				if !yield(k, v) {
					return
				}
			}
		}
	}
}

func Map2[K1, V1, K2, V2 any](mapFunc func(K1, V1) (K2, V2), s iter.Seq2[K1, V1]) iter.Seq2[K2, V2] {
	return func(yield func(K2, V2) bool) {
		for k1, v1 := range s {
			k2, v2 := mapFunc(k1, v1)
			if !yield(k2, v2) {
				return
			}
		}
	}
}
