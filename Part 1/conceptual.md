### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
    * ```A RESTful route is a route that provides mapping between HTTP verbs (get, post, put, delete, patch) to controller CRUD actions (create, read, update, delete). Instead of relying solely on the URL to indicate what site to visit, a RESTful route also depends on the HTTP verb and the URL```

- What is a resource?
    * ```A resource is an object with a type, associated data, relationships to other resources, and a set of methods that operate on it. It is similar to an object instance in an object-oriented programming language, with the important difference that only a few standard methods are defined for the resource (corresponding to the standard HTTP GET, POST, PUT and DELETE methods), while an object instance typically has many methods.```

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
    * ```If the user somehow refreshed the page or revisit the route multiple times at once, a post requests would be made each time which can lead to multiple new users being made.```

- What does idempotent mean? Which HTTP verbs are idempotent?
    * ```An idempotent operation can be performed many times (with same data) with the result of all calls being the same as if it was done once. GET requests are examples of idempotent operations```

- What is the difference between PUT and PATCH?
    * ```PATCH is used to update an existing entity with new information. You can't PATCH request an entity that does not exist. An example of PATCH would be updating a user's user name. PUT is used to replace an entity's information entirely```

- What is one way encryption?
    * ```One-way encryption or one-way hash function is designed in a manner that is hard to reverse the process, that is to find a string that hashes to a given value. Two exactly similar values should have the same output.```

- What is the purpose of a `salt` when hashing a password?
    * ``` `salt` is a randomly generated string introduced before hashing. Typically would concatenate the `salt` string to the password then hash the two together.```

- What is the purpose of the Bcrypt module?
    * ```Bcrypt is a password hashing algorithm that allows you to choose how many rounds of encryption should be ran to encrypt passwords.```

- What is the difference between authorization and authentication?
    * ```Authentication means confirming your identity while authentication means being allowed access.```

- What are some ways to manage the complexities of a large codebase, like Warbler?
    * ```Keep code clean, apply test-driven development, use functions to abstract complexity, and make smaller and more frequent commits```