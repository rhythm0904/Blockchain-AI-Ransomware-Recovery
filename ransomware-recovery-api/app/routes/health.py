from flask import Blueprint, jsonify

bp = Blueprint("health", __name__)

@bp.get("/")
def root():
    return jsonify(message="Blockchain + AI Ransomware Recovery API is running!")

@bp.get("/health")
def health():
    return jsonify(status="ok")
