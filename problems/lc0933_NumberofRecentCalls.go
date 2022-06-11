package problems

import "container/list"

type RecentCounter struct {
	recentCalls *list.List
}

func Constructor() RecentCounter {
	return RecentCounter{recentCalls: list.New()}
}

func (this *RecentCounter) Ping(t int) int {
	earliestCallTimestamp := t - 3000
	for this.recentCalls.Len() > 0 && this.recentCalls.Front().Value.(int) < earliestCallTimestamp {
		this.recentCalls.Remove(this.recentCalls.Front())
	}
	this.recentCalls.PushBack(t)
	return this.recentCalls.Len()
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
