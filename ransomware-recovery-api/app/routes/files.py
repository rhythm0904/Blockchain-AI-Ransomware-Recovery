from flask import Blueprint, jsonify, request
from ..services.store import store

bp = Blueprint("files", __name__)

@bp.get("")
def list_files():
    items = store.list_files()
    return jsonify(items=items, count=len(items))

@bp.post("")
def add_file():
    data = request.get_json(silent=True) or {}
    filename = data.get("filename")
    status = data.get("status", "clean")
    notes = data.get("notes")

    if not filename:
        return jsonify(error="filename is required"), 400

    item = store.add_file(filename, status=status, notes=notes)
    return jsonify(message="File stored", item=item), 201

@bp.get("/<string:filename>")
def get_file(filename):
    item = store.get_file(filename)
    if not item:
        return jsonify(error="File not found"), 404
    return jsonify(item=item)

@bp.delete("/<string:filename>")
def delete_file(filename):
    ok = store.delete_file(filename)
    if not ok:
        return jsonify(error="File not found"), 404
    return jsonify(message="Deleted", filename=filename)
