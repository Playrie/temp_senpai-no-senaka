# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `rails
# db:schema:load`. When creating a new database, `rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2021_07_11_015257) do

  create_table "follows", force: :cascade do |t|
    t.integer "from_kerbero_id"
    t.integer "to_kerbero_id"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "kerberos", force: :cascade do |t|
    t.string "name"
    t.string "common_password"
    t.string "confirm_password"
    t.boolean "is_male"
    t.integer "sex_num"
    t.integer "left_user_id", default: 0, null: false
    t.integer "center_user_id", default: 0, null: false
    t.integer "right_user_id", default: 0, null: false
    t.boolean "is_confirmed", default: false, null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.integer "age"
    t.index ["name"], name: "index_kerberos_on_name", unique: true
  end

  create_table "undecided_schedules", force: :cascade do |t|
    t.string "date"
    t.integer "user_id"
    t.string "start_time"
    t.string "end_time"
    t.boolean "is_confirmed", default: false, null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "position"
    t.integer "kerbero_id"
    t.boolean "is_set_id", default: false, null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

end
