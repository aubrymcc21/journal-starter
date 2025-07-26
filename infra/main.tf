provider "azurerm" {
  features {}

  subscription_id = "2a752143-c3fe-4d4f-82ee-ac858b81bad7"
}

resource "azurerm_resource_group" "rg" {
  name     = "journal-app-rg"
  location = "eastus"
}