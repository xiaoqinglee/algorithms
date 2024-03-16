# https://leetcode.cn/problems/kth-largest-element-in-an-array/
defmodule Solution do
  @spec find_kth_largest(nums :: [integer], k :: integer) :: integer
  def find_kth_largest(nums, k) do
    true = is_integer(k) and 0 < k and k <= length(nums)

    tree =
      Enum.reduce(nums, :gb_trees.empty(), fn
        num, tree ->
          cond do
            :gb_trees.size(tree) == k ->
              {_, smallest_num} = :gb_trees.smallest(tree)

              cond do
                smallest_num < num ->
                  {_, _, temp_tree} = :gb_trees.take_smallest(tree)
                  :gb_trees.insert({num, :erlang.unique_integer()}, num, temp_tree)

                true ->
                  tree
              end

            true ->
              :gb_trees.insert({num, :erlang.unique_integer()}, num, tree)
          end
      end)

    {_, result} = :gb_trees.smallest(tree)
    result
  end
end

Solution.find_kth_largest([3, 2, 1, 5, 6, 4], 2)
|> dbg()

# http://erlang.org/pipermail/erlang-questions/2007-July/027720.html

# Subject: Re: [erlang-questions] Priority queue

# You can use a gb_trees structure:

# in(Item, Prio, Q) ->
#    gb_trees:insert({Prio,now()}, Item, Q).

# out(Q) ->
#    gb_trees:take_smallest(Q).

# peek(Q) ->
#    gb_trees:smallest(Q).

# The order will be FIFO. If you want LIFO, you
# could negate the Prio value and take_largest
# instead.

# https://learnyousomeerlang.com/time
# The new components of the VM are exposed to the user with the following functions:
# erlang:unique_integer() and erlang:unique_integer(Options), which returns unique values.
