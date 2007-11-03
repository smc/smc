SCIM_TABLES_DIR=/usr/share/scim/tables
SCIM_ICONS_DIR=/usr/share/scim/icons

SRC_DIR=.
BIN_DIR=.
ICON_DIR=.

SCIM_MAKE_TABLE=scim-make-table

compile: compile-Malayalam-inscript

compile-Malayalam-inscript: $(BIN_DIR)/Malayalam-inscript.bin

install: install-Malayalam-inscript
uninstall: uninstall-Malayalam-inscript

install-Malayalam-inscript: compile-Malayalam-inscript
	cp $(BIN_DIR)/Malayalam-inscript.bin $(SCIM_TABLES_DIR)
	cp $(ICON_DIR)/Malayalam-inscript.png $(SCIM_ICONS_DIR)

uninstall-Malayalam-inscript:
	rm $(SCIM_TABLES_DIR)/Malayalam-inscript.bin
	rm $(SCIM_ICONS_DIR)/Malayalam-inscript.png


clean:
	rm -f $(BIN_DIR)/*

$(BIN_DIR)/Malayalam-inscript.bin: $(SRC_DIR)/Malayalam-inscript.txt.in
	mkdir -p  $(BIN_DIR)
	sed -e \\'s,@SCIM_ICONDIR@,$(SCIM_ICONS_DIR),g\\' $(SRC_DIR)/Malayalam-inscript.txt.in > $(BIN_DIR)/Malayalam-inscript.txt
	$(SCIM_MAKE_TABLE) $(BIN_DIR)/Malayalam-inscript.txt -b -o $(BIN_DIR)/Malayalam-inscript.bin
	rm $(BIN_DIR)/Malayalam-inscript.txt
