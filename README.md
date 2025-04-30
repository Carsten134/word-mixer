## Perfect Match inspired wordmixer
This is a small word mixer, that I coded in an afternoon. Check out the [Demo and motivation](https://youtu.be/V8QL4-l3_uA).

## How it works
Given two word embeddings $\vec{x}, \vec{y}$ and a mixture coefficient $\alpha$ we "mix" these two embeddings by taking the weighted average:

$$
\vec{z} := \alpha\vec{x}+ (1-\alpha)\vec{y}
$$

The higher $\alpha$ the more $\vec{z}$ will point towards $\vec{x}$. And the lower $\alpha$ the more the vector will point towards $\vec{y}$. We get the mixed words, by just searching for embeddings, that point in the same direction as $\vec z$ (so with the highest cos-similarity).

## Structure
This webapp consists of a locally restful flask API, that exposes an endpoint to mix the two words, and a nuxt frontend. The user has two text inputs to enter the words and a slider, to adjust the mixture.
 