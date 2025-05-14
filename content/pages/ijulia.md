Title: Types in Julia
Date: 2025-05-13 10:20
Category: Julia
Tags: julia, jupyter
Slug: my-super-post
Authors: Hugo
Summary: Some tips on types



# Julia Types


## Julia Inner constructors once and for all 
 
Confusion surrounding the `new` keyword


## Parametric Types 

- You choose the types Supertype and then can pick and choose for instance 

```julia 
struct Point{T <: Real}
    x::T
    y::T
end
```

# Julia regex 

`ismatch(regex, string)`


# Graphs 

- Graphs.jl exploration 


# Stats 

[An article for reference](https://datawookie.dev/blog/2015/10/monthofjulia-day-28-hypothesis-tests/)
