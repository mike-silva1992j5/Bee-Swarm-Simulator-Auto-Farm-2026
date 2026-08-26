-- Build: 8a26e01c7fd5baa371cd69e36738a40d
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
