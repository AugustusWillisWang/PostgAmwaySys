// 0:26:29
// 湘-847-资威 2017/6/27 0:26:29
package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	// calculate the memory occupation state
	runtime.GC()
	var m0 runtime.MemStats
	runtime.ReadMemStats(&m0)

	var large_array = make([]int, 128*1024*1024)
	// array initialization, 1024 MB space
	for i := 0; i < len(large_array); i++ {
		large_array[i] = rand.Int()
	}

	// sort the array in a ascending order
	start := time.Now()

	// n*log_2(n) = 3623878656
	quicksort(large_array[0:])

	elapsed := time.Since(start)

	runtime.GC()
	var m1 runtime.MemStats
	runtime.ReadMemStats(&m1)
	memUsage := m1.Alloc - m0.Alloc

	fmt.Printf("Sort took %.3f seconds\n", float64(elapsed)/1000/1000/1000)
	fmt.Printf("Cost memory %.3f MB\n", float64(memUsage)/1024/1024)

	// Check whether the array is ordered
	// TODO Your code here
	for i := 0; i < len(large_array)-1; i++ {
		if large_array[i] > large_array[i+1] {
			fmt.Println(large_array[i], large_array[i+1])
			break
		}
	}
}

// sort the array in place, the array will be
// ordered after the return of the function
func quicksort(array []int) []int {
	// TODO Your code here

	if len(array) <= 2 {
		if (len(array) == 2) && (array[0] <= array[1]) {
			return array
		} else if (len(array) == 2) && (array[0] > array[1]) {
			r := array[0]
			array[0] = array[1]
			array[1] = r
			return array
		} else {
			return array
		}
	} else {
		q := par(array)

		for i := 0; i < len(array); i++ {
			fmt.Println(array[i])
		}
		fmt.Println(q, "mid")
		fmt.Println("endline")

		quicksort(array[0:q])
		quicksort(array[q+1:])
		return array
	}
}
func par(array []int) int {
	if len(array) <= 1 {
		return 0
	} else {
		g1 := 0
		g2 := len(array) - 1
		global := 0
		for i, j, k := 0, 1, 2; g1 != g2; i = g1 {
			for j = len(array) - 1; (array[i] <= array[j]) && (j > i); j-- {

			}
			fmt.Println(i)

			m := array[j]
			array[j] = array[i]
			array[i] = m
			for k = 0; (array[k] <= array[j]) && (k < j); k++ {
			}
			fmt.Println(k, "k")
			//fmt.Println(k)

			n := array[k]
			array[k] = array[j]
			array[j] = n
			fmt.Println(k, "k")
			g1 = k
			g2 = j
			global = k
		}
		return global
	}
}
