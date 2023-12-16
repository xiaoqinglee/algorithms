# https://leetcode.cn/problems/two-sum
defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    nums
    |> Stream.with_index()
    |> Enum.reduce_while(_init_acc = %{}, fn _x = {num, num_idx}, _acc = map ->
      other_num = target - num

      case map do
        %{^other_num => other_num_idx} -> {:halt, _result = [other_num_idx, num_idx]}
        _ -> {:cont, _new_acc = Map.put(map, num, num_idx)}
      end
    end)
  end
end

[2, 7, 11, 15]
|> Solution.two_sum(9)
|> dbg()

# in project home directory, run:
# mix format
# elixir lib/Map/lc0001_TwoSum.exs
