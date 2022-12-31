"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Logger = void 0;
const vscode_1 = require("vscode");
class Logger {
    static getInstance() {
        Logger.instance = Logger.instance ?? new Logger();
        return Logger.instance;
    }
    constructor() {
        this.out = vscode_1.window.createOutputChannel("Git Blame");
    }
    static error(error) {
        if (error instanceof Error) {
            Logger.write("error", error.toString());
        }
    }
    static write(level, message) {
        Logger.getInstance().out.appendLine(`[ ${(new Date).toTimeString().substr(0, 8)} | ${level} ] ${message.trim()}`);
    }
    dispose() {
        Logger.instance = undefined;
        this.out.dispose();
    }
}
exports.Logger = Logger;
//# sourceMappingURL=logger.js.map