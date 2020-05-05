function snakeToCamel(snake) {
    const regex = /([-_]\w)/g;
    let camel = snake.replace((regex), g => g[1].toUpperCase());

    return camel;
}