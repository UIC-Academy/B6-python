words = ["eshmat", "gishmat", "gulchapchap", "somsabek", "hi", "vali"]

sorted_words = sorted(
    words, 
    key=lambda w: len(w),
    reverse=True
)

print(sorted_words)


word = "hello"


"""
typedef struct {
    char *content
    int length
} PyObject;

PyObject word = {
    .content = "hello,
    .length = 5
}
"""