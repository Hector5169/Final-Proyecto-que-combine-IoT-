// mcp.js
const MCP = (() => {
    const PRODUCTO_KEY = "producto_actual";
    const RESENAS_KEY_PREFIX = "resenas_";

    function setProducto(producto) {
        localStorage.setItem(PRODUCTO_KEY, JSON.stringify(producto));
    }

    function getProducto() {
        return JSON.parse(localStorage.getItem(PRODUCTO_KEY));
    }

    function getResenas(id) {
        return JSON.parse(localStorage.getItem(`${RESENAS_KEY_PREFIX}${id}`)) || [];
    }

    function agregarResena(id, resena) {
        const resenas = getResenas(id);
        resenas.push(resena);
        localStorage.setItem(`${RESENAS_KEY_PREFIX}${id}`, JSON.stringify(resenas));
    }

    return {
        setProducto,
        getProducto,
        getResenas,
        agregarResena,
    };
})();