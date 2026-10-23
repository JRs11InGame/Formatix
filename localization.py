import locale

APP_NAME = "Formatix"

LANGUAGES = {
    "en": "English",
    "es": "Español"
}

STRINGS = {
    "en": {
        "add": "+ Add", "clear": "✕ Clear", "src_panel": " Source files", "dst_panel": "✅ Result",
        "save_folder": "SAVE TO FOLDER", "folder_placeholder": "not selected — will ask on convert",
        "pick_dir": " Choose", "format_lbl": "FORMAT", "quality_lbl": "QUALITY", "resize_lbl": "RESIZE",
        "progress_lbl": "PROGRESS", "filesize_lbl": "FILE SIZE", "was": "Was:", "became": "Became:",
        "convert_btn": "▶ Convert", "processing_btn": "▶ Processing...", "stop_btn": "■ Stop",
        "col_filename": "File name", "col_res": "Resolution", "col_size": "Size", "col_status": "Status",
        "drop_hint": "Drag images here\nor click to browse", "drop_release": "Drop files here!",
        "ready": "Ready", "files_count": "Files: {n}", "cleared": "List cleared", "warn_no_files": "Add files first!",
        "warn_bad_size": "Please enter width and height values.", "overwrite_title": "Files exist",
        "overwrite_msg": "The following files already exist in the target folder: {names}. Overwrite?",
        "overwrite_more": "\n... and {n} more", "resize_no_change": "No changes",
        "resize_prop_w": "Proportional (by width)", "resize_prop_h": "Proportional (by height)",
        "resize_crop": "Smart crop (Fill)", "settings_title": "Settings", "settings_lang": "Interface language",
        "donate_title": "Support development", "donate_sub": f"Thanks for using {APP_NAME}!",
        "donate_desc": "If this program saved you time, you can\nsupport its development:",
        "donate_copied": "Address copied!", "donate_btn": "Open wallets page", "auto": "Auto",
        "cache_tag": " (cache)", "resize_custom": "Custom", "ico_too_large_title": "ICO size limit",
        "ico_too_large_msg": "ICO format does not support resolutions above 256×256.\nThe image will be resized to fit.",
        "ico_too_large_cancel": "Cancel", "ico_too_large_ok": "OK", "settings_remember": "Remember settings",
        "settings_theme": "Theme", "theme_dark": "Dark", "theme_light": "Light",
        "theme_restart_note": "Restart the application to apply the new theme.",
        "settings_check_updates": "Check for updates automatically", "update_check_now": "Check now",
        "update_checking": "Checking...", "update_up_to_date": "You have the latest version",
        "update_check_failed": "Could not check for updates", "update_ver_label": "update v{old} -> {new} available",
        "svg_no_size_title": "SVG: size required", "svg_no_size_msg": "SVG files do not have a fixed resolution.\nPlease set width and height in 'Custom' mode before converting.",
        "compare_btn": " Compare", "compare_title": "Comparison", "compare_no_files": "No files to compare",
        "qmode_percent": "%", "qmode_size": "Size", "warn_bad_target_size": "Please enter a valid target file size (greater than 0).",
        "settings_filename_lbl": "File name", "fn_preset_original": "Keep as is",
        "fn_preset_number": "Name + sequence number", "fn_preset_date": "Name + date", "fn_preset_custom": "Custom template...",
        "fn_add_name": "File name", "fn_add_index": "Index", "fn_add_date": "Date", "fn_add_text": "Custom text...",
        "fn_clear": "Clear", "fn_preview_lbl": "Preview:", "fn_custom_text_prompt": "Enter text to insert",
        "fn_empty_hint": "Click a button above to build a template"
    },
    "es": {
        "add": "+ Añadir", "clear": "✕ Limpiar", "src_panel": " Archivos de origen", "dst_panel": "✅ Resultado",
        "save_folder": "GUARDAR EN CARPETA", "folder_placeholder": "no seleccionada — se preguntará al convertir",
        "pick_dir": " Elegir", "format_lbl": "FORMATO", "quality_lbl": "CALIDAD", "resize_lbl": "CAMBIAR RESOLUCIÓN",
        "progress_lbl": "PROGRESO", "filesize_lbl": "TAMAÑO DEL ARCHIVO", "was": "Antes:", "became": "Después:",
        "convert_btn": "▶ Convertir", "processing_btn": "▶ Procesando...", "stop_btn": "■ Detener",
        "col_filename": "Nombre del archivo", "col_res": "Resolución", "col_size": "Tamaño", "col_status": "Estado",
        "drop_hint": "Arrastra las imágenes aquí\no haz clic para buscar", "drop_release": "¡Suelta los archivos aquí!",
        "ready": "Listo", "files_count": "Archivos: {n}", "cleared": "Lista limpiada", "warn_no_files": "¡Añade archivos primero!",
        "warn_bad_size": "Por favor, introduce valores de ancho y alto.", "overwrite_title": "Los archivos existen",
        "overwrite_msg": "Los siguientes archivos ya existen en la carpeta de destino: {names}. ¿Reemplazarlos?",
        "overwrite_more": "\n... y {n} más", "resize_no_change": "Sin cambios",
        "resize_prop_w": "Proporcional (por ancho)", "resize_prop_h": "Proporcional (por alto)",
        "resize_crop": "Recorte inteligente (Rellenar)", "settings_title": "Ajustes", "settings_lang": "Idioma de la interfaz",
        "donate_title": "Apoyar el desarrollo", "donate_sub": f"¡Gracias por usar {APP_NAME}!",
        "donate_desc": "Si el programa te ahorró tiempo, puedes\napoyar su desarrollo:", "donate_copied": "¡Dirección copiada!",
        "donate_btn": "Abrir página con monederos", "auto": "Auto", "cache_tag": " (caché)", "resize_custom": "Personalizado",
        "ico_too_large_title": "Límite de tamaño ICO", "ico_too_large_msg": "El formato ICO no admite resoluciones superiores a 256×256.\nLa imagen se redimensionará para ajustarse.",
        "ico_too_large_cancel": "Cancelar", "ico_too_large_ok": "Aceptar", "settings_remember": "Recordar ajustes",
        "settings_theme": "Tema", "theme_dark": "Oscuro", "theme_light": "Claro",
        "theme_restart_note": "Reinicia la aplicación para aplicar el nuevo tema.",
        "settings_check_updates": "Buscar actualizaciones auto.", "update_check_now": "Buscar ahora",
        "update_checking": "Buscando…", "update_up_to_date": "Tienes la última versión",
        "update_check_failed": "No se pudieron buscar actualizaciones", "update_ver_label": "actualización v{old} → {new} disponible",
        "svg_no_size_title": "SVG: se requiere tamaño", "svg_no_size_msg": "Los archivos SVG no tienen una resolución fija.\nPor favor, establece el ancho y el alto en el modo «Personalizado» antes de convertir.",
        "compare_btn": " Comparar", "compare_title": "Comparación", "compare_no_files": "No hay archivos para comparar",
        "qmode_percent": "%", "qmode_size": "Tamaño", "warn_bad_target_size": "Por favor, introduce un tamaño de archivo objetivo válido (mayor que 0).",
        "settings_filename_lbl": "Nombre del archivo", "fn_preset_original": "Mantener como está",
        "fn_preset_number": "Nombre + número de secuencia", "fn_preset_date": "Nombre + fecha", "fn_preset_custom": "Plantilla personalizada…",
        "fn_add_name": "Nombre del archivo", "fn_add_index": "Número", "fn_add_date": "Fecha", "fn_add_text": "Texto personalizado…",
        "fn_clear": "Limpiar", "fn_preview_lbl": "Vista previa:", "fn_custom_text_prompt": "Introduce el texto a insertar",
        "fn_empty_hint": "Haz clic en un botón de arriba para construir una plantilla"
    }
}

def detect_system_lang():
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.lower().startswith("es"):
            return "es"
    except Exception:
        pass
    return "en"

def t(key, lang="en", **kwargs):
    text = STRINGS.get(lang, STRINGS["en"]).get(key, STRINGS["en"].get(key, key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except KeyError:
            return text
    return text