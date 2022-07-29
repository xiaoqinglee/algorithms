package main

import (
	"container/list"
	"fmt"
	"github.com/davecgh/go-spew/spew"
	"github.com/k0kubun/pp/v3"
)

func main() {

	obj := list.New()
	obj.PushFront(42)
	spew.Config = spew.ConfigState{Indent: "    "}

	spew.Dump(obj)
	pp.Println(obj)

	fmt.Println("=============================================")
	spew.Dump(obj)
	pp.Println(obj)

}
