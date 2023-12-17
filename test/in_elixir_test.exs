defmodule InElixirTest do
  use ExUnit.Case
  doctest InElixir

  test "greets the world" do
    assert InElixir.hello() == :world
  end
end
