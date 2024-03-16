# https://leetcode.cn/problems/group-anagrams
defmodule Solution do
  @spec group_anagrams(strs :: [String.t()]) :: [[String.t()]]
  def group_anagrams(strs) do
    strs
    |> Enum.reduce(%{}, fn str, map ->
      key = str |> String.to_charlist() |> Enum.sort() |> List.to_string()
      Map.update(map, key, [str], &[str | &1])
    end)
    |> Map.values()
  end
end
