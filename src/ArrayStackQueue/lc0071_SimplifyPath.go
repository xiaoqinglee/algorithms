package ArrayStackQueue

import (
	"github.com/xiaoqinglee/algorithms/pkg"
	"slices"
	"strings"
)

// https://leetcode.cn/problems/simplify-path
func simplifyPath(path string) string {
	var folders []string
	if strings.HasPrefix(path, "/") {
		folders = append(folders, "/")
	}
	isValidFolderName := func(s string) bool {
		return s != ""
	}
	folders = slices.AppendSeq(folders, pkg.Filter(isValidFolderName, strings.SplitSeq(path, "/")))
	var newFolders []string
	for _, folder := range folders {
		switch folder {
		case ".":
			//do nothing
		case "..":
			if len(newFolders) > 0 {
				if newFolders[len(newFolders)-1] == "/" {
					//do nothing
				} else {
					newFolders = newFolders[:len(newFolders)-1]
				}
			} else {
				panic("invalid path")
			}
		default:
			newFolders = append(newFolders, folder)
		}
	}

	if folders[0] == "/" {
		return "/" + strings.Join(newFolders[1:], "/")
	} else {
		return strings.Join(newFolders, "/")
	}
}

func TestSimplifyPath() {
	testCases := map[string]string{
		"/home/":                           "/home",
		"/home//foo/":                      "/home/foo",
		"/home/user/Documents/../Pictures": "/home/user/Pictures",
		"/../":                             "/",
		"/.../a/../b/c/../d/./":            "/.../b/d",
	}
	for k, v := range testCases {
		if simplifyPath(k) != v {
			panic("wrong impl")
		}
	}
}
