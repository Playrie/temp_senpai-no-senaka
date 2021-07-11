class CreateKerberos < ActiveRecord::Migration[6.0]
  def change
    create_table :kerberos do |t|
      t.string :name
      t.string :common_password
      t.string :confirm_password
      t.boolean :is_male
      t.integer :sex_num

      t.integer :left_user_id,      null: false, default: 0
      t.integer :center_user_id,    null: false, default: 0
      t.integer :right_user_id,     null: false, default: 0

      t.boolean :is_confirmed, null: false, default: false

      t.timestamps
    end
    add_index :kerberos, [:name], unique: true
  end
end
