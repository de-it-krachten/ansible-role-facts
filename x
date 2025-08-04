yq -j . .cicd > /tmp/1
yq -j . .cicd.overwrite > /tmp/2

jq -s '
def deepmerge(a; b):
  reduce (b | to_entries[]) as $entry
    (a;
     if (a[$entry.key]? | type == "object" and $entry.value | type == "object") then
       .[$entry.key] = deepmerge(a[$entry.key]; $entry.value)
     else
       .[$entry.key] = $entry.value
     end);
deepmerge(.[0]; .[1])
' /tmp/1 /tmp/2
